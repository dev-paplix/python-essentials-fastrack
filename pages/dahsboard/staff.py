from jwt import verify_token
from database import get_all_users


def handle_staff_dashboard(token: str) -> tuple[dict, int]:
    """
    Handle staff dashboard data request. Requires valid staff JWT.
    """
    if not token:
        return {"success": False, "error": "Authorization token required"}, 401

    try:
        claims = verify_token(token)
    except ValueError as e:
        return {"success": False, "error": str(e), "expired": "expired" in str(e).lower()}, 401

    if claims.get("type") != "staff":
        return {"success": False, "error": "Access forbidden: Staff role required"}, 403

    all_users = get_all_users()
    staff_count = sum(1 for u in all_users if u["user_type"] == "staff")
    customer_count = sum(1 for u in all_users if u["user_type"] == "customer")

    return {
        "success": True,
        "role": "staff",
        "email": claims.get("email"),
        "expires_at": claims.get("exp"),
        "dashboard": {
            "title": "Staff Management Portal",
            "stats": {
                "total_users": len(all_users),
                "staff_count": staff_count,
                "customer_count": customer_count,
                "system_status": "Online (Active Session: 120s idle timeout)"
            },
            "recent_users": all_users[:10]
        }
    }, 200

