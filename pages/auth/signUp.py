import re
import sqlite3
from database import insert_user, find_user_by_email
from jwt import create_token


def handle_sign_up(body: dict) -> tuple[dict, int]:
    """
    Register a new user (staff or customer) and issue an initial 120-second JWT.
    Returns (response_data, status_code).
    """
    email = body.get("email", "").strip().lower()
    password = body.get("password", "")
    user_type = body.get("type", "").strip().lower()

    if not email:
        return {"success": False, "error": "Email is required."}, 400

    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return {"success": False, "error": "Invalid email address format."}, 400

    if not password or len(password) < 6:
        return {"success": False, "error": "Password must be at least 6 characters long."}, 400

    if user_type not in ("staff", "customer"):
        return {"success": False, "error": "User type must be either 'staff' or 'customer'."}, 400

    existing = find_user_by_email(email)
    if existing:
        return {"success": False, "error": "An account with this email already exists."}, 409

    try:
        new_user = insert_user(email, password, user_type)
    except sqlite3.IntegrityError:
        return {"success": False, "error": "Email is already registered."}, 409
    except Exception as e:
        return {"success": False, "error": f"Registration failed: {str(e)}"}, 500

    # Auto-login with 120-second token
    token = create_token({
        "email": new_user["email"],
        "type": user_type
    }, expires_in=120)

    redirect_url = "/pages/dahsboard/staff.js" if user_type == "staff" else "/pages/dahsboard/customer.js"

    return {
        "success": True,
        "message": f"Account successfully created as {user_type.capitalize()}!",
        "token": token,
        "user": {
            "id": new_user["id"],
            "email": new_user["email"],
            "type": user_type
        },
        "redirect": redirect_url
    }, 201

