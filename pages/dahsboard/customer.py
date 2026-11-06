from jwt import verify_token
from database import find_user_by_email


def handle_customer_dashboard(token: str) -> tuple[dict, int]:
    """
    Handle customer dashboard data request. Requires valid customer JWT.
    """
    if not token:
        return {"success": False, "error": "Authorization token required"}, 401

    try:
        claims = verify_token(token)
    except ValueError as e:
        return {"success": False, "error": str(e), "expired": "expired" in str(e).lower()}, 401

    if claims.get("type") != "customer":
        return {"success": False, "error": "Access forbidden: Customer role required"}, 403

    user = find_user_by_email(claims.get("email"))

    return {
        "success": True,
        "role": "customer",
        "email": claims.get("email"),
        "expires_at": claims.get("exp"),
        "dashboard": {
            "title": "Customer Self-Service Hub",
            "account": {
                "member_id": f"CUST-{user['id']:04d}" if user else "CUST-0001",
                "tier": "Gold Member",
                "member_since": user["created_at"] if user else "2026-11-06",
                "reward_points": 1250,
                "session_timeout": "120s inactivity limit"
            },
            "orders": [
                {"id": "ORD-9901", "service": "Python FastTrack Training", "status": "In Progress", "amount": "RM 4,500.00"},
                {"id": "ORD-9884", "service": "API Gateway Consultation", "status": "Completed", "amount": "RM 2,800.00"}
            ]
        }
    }, 200

