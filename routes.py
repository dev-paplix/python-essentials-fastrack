import json
import os
from pathlib import Path
from robyn import Response, Headers, Request

# Backend route logic imports
from pages.auth.signIn import handle_sign_in
from pages.auth.signUp import handle_sign_up
from pages.dahsboard.staff import handle_staff_dashboard
from pages.dahsboard.customer import handle_customer_dashboard
from pages.ocr_service import handle_ocr_request
from jwt import verify_token

BASE_DIR = Path(__file__).parent.resolve()


def _json_response(data: dict, status: int = 200) -> Response:
    return Response(
        status_code=status,
        headers=Headers({"Content-Type": "application/json; charset=utf-8"}),
        description=json.dumps(data)
    )


def _file_response(path: Path, content_type: str) -> Response:
    if not path.exists():
        return Response(
            status_code=404,
            headers=Headers({"Content-Type": "text/plain"}),
            description="404 Not Found"
        )
    with open(path, "r", encoding="utf-8") as f:
        return Response(
            status_code=200,
            headers=Headers({"Content-Type": content_type}),
            description=f.read()
        )


def _parse_body(request: Request) -> dict:
    try:
        if hasattr(request, "json"):
            res = request.json()
            if callable(res):
                res = res()
            if isinstance(res, dict):
                return res
        if hasattr(request, "body"):
            body = request.body
            if isinstance(body, (bytes, bytearray)):
                body = body.decode("utf-8")
            if isinstance(body, str) and body.strip():
                return json.loads(body)
    except Exception:
        pass
    return {}


def _extract_token(request: Request) -> str:
    headers = getattr(request, "headers", None)
    if not headers:
        return ""
    auth = ""
    if hasattr(headers, "get"):
        auth = headers.get("authorization") or headers.get("Authorization") or ""
    elif isinstance(headers, dict):
        auth = headers.get("authorization") or headers.get("Authorization") or ""
    if auth.startswith("Bearer "):
        return auth[7:].strip()
    return auth.strip()


def register_routes(app):
    """Register all frontend and API routes onto the Robyn application."""

    # -------------------------------------------------------------
    # Frontend Pages and Vanilla JS Servicing
    # -------------------------------------------------------------
    @app.get("/")
    async def serve_index(request: Request):
        return _file_response(BASE_DIR / "index.html", "text/html; charset=utf-8")

    @app.get("/index.js")
    async def serve_index_js(request: Request):
        return _file_response(BASE_DIR / "index.js", "application/javascript; charset=utf-8")

    @app.get("/pages/auth/signIn.js")
    async def serve_signin_js(request: Request):
        return _file_response(BASE_DIR / "pages" / "auth" / "signIn.js", "application/javascript; charset=utf-8")

    @app.get("/pages/auth/signUp.js")
    async def serve_signup_js(request: Request):
        return _file_response(BASE_DIR / "pages" / "auth" / "signUp.js", "application/javascript; charset=utf-8")

    @app.get("/pages/dahsboard/staff.js")
    async def serve_staff_js(request: Request):
        return _file_response(BASE_DIR / "pages" / "dahsboard" / "staff.js", "application/javascript; charset=utf-8")

    @app.get("/pages/dahsboard/customer.js")
    async def serve_customer_js(request: Request):
        return _file_response(BASE_DIR / "pages" / "dahsboard" / "customer.js", "application/javascript; charset=utf-8")

    @app.get("/pages/ocrService.js")
    async def serve_ocr_js(request: Request):
        return _file_response(BASE_DIR / "pages" / "ocrService.js", "application/javascript; charset=utf-8")

    # -------------------------------------------------------------
    # Authentication Endpoints (delegated to pages/auth/*.py)
    # -------------------------------------------------------------
    @app.post("/api/auth/signin")
    async def api_signin(request: Request):
        body = _parse_body(request)
        data, status = handle_sign_in(body)
        return _json_response(data, status)

    @app.post("/api/auth/signup")
    async def api_signup(request: Request):
        body = _parse_body(request)
        data, status = handle_sign_up(body)
        return _json_response(data, status)

    @app.get("/api/auth/me")
    async def api_me(request: Request):
        token = _extract_token(request)
        if not token:
            return _json_response({"success": False, "error": "No token provided"}, 401)
        try:
            claims = verify_token(token)
            return _json_response({"success": True, "user": claims}, 200)
        except ValueError as e:
            return _json_response({"success": False, "error": str(e)}, 401)

    # -------------------------------------------------------------
    # Dashboard Endpoints (delegated to pages/dahsboard/*.py)
    # -------------------------------------------------------------
    @app.get("/api/dashboard/staff")
    async def api_staff_dashboard(request: Request):
        token = _extract_token(request)
        data, status = handle_staff_dashboard(token)
        return _json_response(data, status)

    @app.get("/api/dashboard/customer")
    async def api_customer_dashboard(request: Request):
        token = _extract_token(request)
        data, status = handle_customer_dashboard(token)
        return _json_response(data, status)

    # -------------------------------------------------------------
    # Gemini AI OCR Endpoint (delegated to pages/ocr_service.py)
    # -------------------------------------------------------------
    @app.post("/api/ocr/extract")
    async def api_ocr_extract(request: Request):
        token = _extract_token(request)
        body = _parse_body(request)
        data, status = handle_ocr_request(body, token)
        return _json_response(data, status)

