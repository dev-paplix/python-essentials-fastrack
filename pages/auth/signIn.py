import json
from database import find_user_by_email, verify_password
from jwt import create_token


def handle_sign_in(body: dict) -> tuple[dict, int]:
    """
    Authenticate user and generate 120-second JWT token.
    Returns (response_data, status_code).
    """
    email = body.get("email", "").strip()
    password = body.get("password", "")

    if not email or not password:
        return {"success": False, "error": "Email and password are required."}, 400

    user = find_user_by_email(email)
    if not user:
        return {"success": False, "error": "Invalid email or password."}, 401

    if not verify_password(password, user["password_hash"]):
        return {"success": False, "error": "Invalid email or password."}, 401

    user_type = user["user_type"]

    # Generate token with 120-second timeout
    token = create_token({
        "email": user["email"],
        "type": user_type
    }, expires_in=120)

    redirect_url = "/pages/dahsboard/staff.js" if user_type == "staff" else "/pages/dahsboard/customer.js"

    return {
        "success": True,
        "message": f"Welcome back, {user_type.capitalize()}!",
        "token": token,
        "user": {
            "id": user["id"],
            "email": user["email"],
            "type": user_type
        },
        "redirect": redirect_url
    }, 200

