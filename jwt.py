import os
import json
import hmac
import hashlib
import base64
import time
from pathlib import Path


def load_env() -> dict:
    """Read key-value pairs from .env file without external dependencies."""
    env_vars = {}
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, val = line.split("=", 1)
                    env_vars[key.strip()] = val.strip().strip("'\"")
    return env_vars


ENV = load_env()
JWT_SECRET = os.environ.get("JWT_SECRET") or ENV.get("JWT_SECRET") or "fasttrack-fallback-secret-key"


def _b64url_encode(data: bytes) -> str:
    """Base64url encode with stripped padding."""
    return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")


def _b64url_decode(encoded_str: str) -> bytes:
    """Base64url decode with recovered padding."""
    rem = len(encoded_str) % 4
    if rem:
        encoded_str += "=" * (4 - rem)
    return base64.urlsafe_b64decode(encoded_str.encode("utf-8"))


def create_token(payload: dict, expires_in: int = 120) -> str:
    """
    Generate an HMAC-SHA256 JWT token.
    Defaults to 120 seconds expiration.
    """
    header = {"alg": "HS256", "typ": "JWT"}
    now = int(time.time())

    claims = dict(payload)
    claims["iat"] = now
    claims["exp"] = now + expires_in

    header_bytes = json.dumps(header, separators=(",", ":")).encode("utf-8")
    payload_bytes = json.dumps(claims, separators=(",", ":")).encode("utf-8")

    enc_header = _b64url_encode(header_bytes)
    enc_payload = _b64url_encode(payload_bytes)

    signing_input = f"{enc_header}.{enc_payload}".encode("utf-8")
    signature = hmac.new(JWT_SECRET.encode("utf-8"), signing_input, hashlib.sha256).digest()
    enc_signature = _b64url_encode(signature)

    return f"{enc_header}.{enc_payload}.{enc_signature}"


def verify_token(token: str) -> dict:
    """
    Verify signature and expiration of JWT token.
    Returns decoded claims dictionary or raises ValueError.
    """
    if not token or not isinstance(token, str):
        raise ValueError("Token is required")

    parts = token.strip().split(".")
    if len(parts) != 3:
        raise ValueError("Invalid JWT structure")

    enc_header, enc_payload, enc_signature = parts

    signing_input = f"{enc_header}.{enc_payload}".encode("utf-8")
    expected_sig = hmac.new(JWT_SECRET.encode("utf-8"), signing_input, hashlib.sha256).digest()

    try:
        actual_sig = _b64url_decode(enc_signature)
    except Exception:
        raise ValueError("Invalid signature encoding")

    if not hmac.compare_digest(expected_sig, actual_sig):
        raise ValueError("Invalid token signature")

    try:
        payload_bytes = _b64url_decode(enc_payload)
        claims = json.loads(payload_bytes.decode("utf-8"))
    except Exception:
        raise ValueError("Corrupt token payload")

    now = int(time.time())
    if "exp" in claims and now > claims["exp"]:
        raise ValueError("Token has expired (120s limit exceeded)")

    return claims


def decode_token_unverified(token: str) -> dict:
    """Decode token payload without verifying signature (for inspection)."""
    parts = token.strip().split(".")
    if len(parts) != 3:
        raise ValueError("Invalid JWT structure")
    payload_bytes = _b64url_decode(parts[1])
    return json.loads(payload_bytes.decode("utf-8"))

