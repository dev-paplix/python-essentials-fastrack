import os
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path
from jwt import verify_token, load_env

# Load environment variables
ENV = load_env()
GOOGLE_TOKEN = os.environ.get("GOOGLE_TOKEN") or ENV.get("GOOGLE_TOKEN") or ""
GOOGLE_LINK = (os.environ.get("GOOGLE_LINK") or ENV.get("GOOGLE_LINK") or "").strip('"')

# Ensure GEMINI_API_KEY is available in the process environment
if GOOGLE_TOKEN and not os.environ.get("GEMINI_API_KEY"):
    os.environ["GEMINI_API_KEY"] = GOOGLE_TOKEN


def _call_gemini_sdk(image_bytes: bytes, mime_type: str) -> str:
    """Execute OCR extraction via the google-genai SDK."""
    from google import genai
    from google.genai import types

    # Initialize client with token from .env
    client = genai.Client(api_key=GOOGLE_TOKEN) if GOOGLE_TOKEN else genai.Client()

    prompt = (
        "You are an expert Optical Character Recognition (OCR) and financial document extraction model. "
        "Extract all information from this invoice or receipt with high precision. "
        "Format the output cleanly with the following sections:\n"
        "1. VENDOR / ISSUER DETAILS\n"
        "2. INVOICE METADATA (Invoice #, Date, Due Date, PO #)\n"
        "3. LINE ITEMS TABLE (Item description, Quantity, Unit Price, Subtotal)\n"
        "4. FINANCIAL TOTALS (Subtotal, Tax / SST / VAT, Shipping, Grand Total)\n"
        "5. FULL RAW TEXT\n\n"
        "Ensure all currency amounts, numbers, and dates are preserved exactly as shown."
    )

    models_to_try = ["gemini-3.6-flash"]
    last_err = None

    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=[
                    types.Part.from_bytes(
                        data=image_bytes,
                        mime_type=mime_type,
                    ),
                    prompt,
                ],
            )
            if response and response.text:
                return response.text
        except Exception as e:
            last_err = e
            continue

    if last_err:
        raise last_err
    raise RuntimeError("No text returned by Gemini SDK")


def _call_gemini_rest(image_base64: str, mime_type: str) -> str:
    """Fallback: Execute OCR directly using the REST endpoint and GOOGLE_LINK from .env."""
    if not GOOGLE_LINK:
        raise ValueError("GOOGLE_LINK is not configured in .env")

    # Add API key to query parameter or header
    endpoint = GOOGLE_LINK
    if GOOGLE_TOKEN and "key=" not in endpoint:
        delimiter = "&" if "?" in endpoint else "?"
        endpoint = f"{endpoint}{delimiter}key={GOOGLE_TOKEN}"

    prompt = (
        "Extract all details from this invoice accurately including vendor, invoice number, "
        "dates, line items, taxes, and total amounts. Format cleanly for copy-pasting."
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": mime_type,
                            "data": image_base64
                        }
                    },
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    req_data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "FastTrack-OCR/1.0"
    }
    if GOOGLE_TOKEN:
        headers["x-goog-api-key"] = GOOGLE_TOKEN

    req = urllib.request.Request(endpoint, data=req_data, headers=headers, method="POST")

    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    # Extract text candidate
    candidates = result.get("candidates", [])
    if candidates:
        parts = candidates[0].get("content", {}).get("parts", [])
        extracted_texts = [p.get("text", "") for p in parts if "text" in p]
        return "\n".join(extracted_texts).strip()

    raise RuntimeError("No text extracted from Gemini REST API response")


def handle_ocr_request(body: dict, auth_token: str) -> tuple[dict, int]:
    """
    Handle invoice upload and OCR extraction for authenticated staff.
    """
    # 1. Verify staff authentication
    if not auth_token:
        return {"success": False, "error": "Authentication token is required"}, 401

    try:
        claims = verify_token(auth_token)
    except ValueError as e:
        return {"success": False, "error": f"Invalid session: {str(e)}"}, 401

    if claims.get("type") != "staff":
        return {"success": False, "error": "Access forbidden: Staff role required for OCR service"}, 403

    # 2. Extract image data
    image_base64 = body.get("image_base64", "").strip()
    mime_type = body.get("mime_type", "image/jpeg").strip()
    filename = body.get("filename", "invoice.jpg")

    if not image_base64:
        return {"success": False, "error": "No image data provided for OCR processing"}, 400

    try:
        image_bytes = base64.b64decode(image_base64)
    except Exception as e:
        return {"success": False, "error": f"Invalid base64 image data: {str(e)}"}, 400

    # 3. Perform OCR with Gemini (SDK first, fallback to REST)
    extracted_text = ""
    engine_used = "google-genai-sdk"

    try:
        extracted_text = _call_gemini_sdk(image_bytes, mime_type)
    except Exception as sdk_error:
        # Fallback to direct REST API if SDK encounter an issue
        try:
            extracted_text = _call_gemini_rest(image_base64, mime_type)
            engine_used = "gemini-rest-endpoint"
        except Exception as rest_error:
            return {
                "success": False,
                "error": f"Gemini OCR failed: SDK Error ({str(sdk_error)}) | REST Error ({str(rest_error)})"
            }, 500

    return {
        "success": True,
        "message": "Invoice processed successfully!",
        "filename": filename,
        "engine": engine_used,
        "extracted_text": extracted_text,
        "extracted_length": len(extracted_text)
    }, 200
