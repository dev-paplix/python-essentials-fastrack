"""
Module 5: Conditional Logic and Flow Control - Student Practice Exercises
Course: Python Essentials FastTrack

Instructions:
1. Complete the challenges below according to their specifications.
2. Run this script to test your logic against the test cases.
"""

# =====================================================================
# Exercise 1: Tiered Volume Discount Calculator
# =====================================================================
# Problem Statement:
# An e-commerce system applies progressive discounts based on purchase quantity:
# - Quantity 1 to 9: 0% discount
# - Quantity 10 to 49: 10% discount
# - Quantity 50 to 99: 15% discount
# - Quantity 100+: 25% discount
# In addition, if the customer is an "executive_member" (bool), they receive an extra
# flat 5% discount on top of their volume discount (e.g., 10% + 5% = 15%).
# Return total price rounded to 2 decimal places.

def calculate_discounted_total(unit_price: float, quantity: int, is_executive: bool) -> float:
    """Calculate order total after volume discount and membership perk."""
    if quantity <= 0:
        return 0.0
        
    discount = 0.0
    if quantity >= 100:
        discount = 0.25
    elif quantity >= 50:
        discount = 0.15
    elif quantity >= 10:
        discount = 0.10
        
    if is_executive:
        discount += 0.05
        
    # Cap maximum discount at 30%
    discount = min(discount, 0.30)
    
    subtotal = unit_price * quantity
    total = subtotal * (1 - discount)
    return round(total, 2)


# =====================================================================
# Exercise 2: Role-Based Access Control (RBAC) Checker
# =====================================================================
# Problem Statement:
# Write a function `check_access(user: dict, resource: str, action: str) -> bool`
# user has keys: "username" (str), "role" (str), "is_active" (bool), "is_mfa_verified" (bool)
# Rules:
# - If `is_active` is False, access is ALWAYS False.
# - If `action` is "DELETE", user MUST have `is_mfa_verified` == True AND `role` == "ADMIN".
# - If `action` is "WRITE", user must have `role` in ("ADMIN", "EDITOR").
# - If `action` is "READ", any active user with role in ("ADMIN", "EDITOR", "VIEWER") has access.
# - Any unknown role or action returns False.

def check_access(user: dict, resource: str, action: str) -> bool:
    """Evaluate permissions based on RBAC and MFA policies."""
    if not user.get("is_active", False):
        return False
        
    role = user.get("role", "").upper()
    action = action.upper()
    mfa = user.get("is_mfa_verified", False)
    
    if action == "DELETE":
        return role == "ADMIN" and mfa
    elif action == "WRITE":
        return role in ("ADMIN", "EDITOR")
    elif action == "READ":
        return role in ("ADMIN", "EDITOR", "VIEWER")
        
    return False


# =====================================================================
# Exercise 3: Password Strength Score Evaluator
# =====================================================================
# Problem Statement:
# Write a function `evaluate_password_security(password: str) -> str`
# Criteria:
# - Length >= 8 chars (+1 point)
# - Length >= 14 chars (+1 point)
# - Contains at least one uppercase letter (+1 point)
# - Contains at least one lowercase letter (+1 point)
# - Contains at least one digit (+1 point)
# - Contains at least one special character from "!@#$%^&*()-_=+" (+1 point)
# Scores:
# - Score <= 2: "VERY WEAK"
# - Score 3-4: "MODERATE"
# - Score >= 5: "STRONG"

def evaluate_password_security(password: str) -> str:
    """Evaluates password complexity score and returns classification string."""
    score = 0
    special_chars = "!@#$%^&*()-_=+"
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 14:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in special_chars for c in password):
        score += 1
        
    if score <= 2:
        return "VERY WEAK"
    elif score <= 4:
        return "MODERATE"
    else:
        return "STRONG"


# =====================================================================
# Verification Test Suite
# =====================================================================
def run_tests():
    print("=" * 60)
    print("RUNNING MODULE 5 PRACTICE TESTS")
    print("=" * 60)

    # Test Exercise 1
    # 5 units @ $100 = $500 (0% discount)
    assert calculate_discounted_total(100.0, 5, False) == 500.0
    # 20 units @ $100 = $2000 - 10% = $1800
    assert calculate_discounted_total(100.0, 20, False) == 1800.0
    # 20 units @ $100 with exec = $2000 - 15% = $1700
    assert calculate_discounted_total(100.0, 20, True) == 1700.0
    print("  [PASS] Exercise 1: Discount Calculator works correctly!")

    # Test Exercise 2
    admin_mfa = {"username": "root", "role": "ADMIN", "is_active": True, "is_mfa_verified": True}
    admin_no_mfa = {"username": "sam", "role": "ADMIN", "is_active": True, "is_mfa_verified": False}
    viewer = {"username": "bob", "role": "VIEWER", "is_active": True, "is_mfa_verified": False}
    inactive = {"username": "eve", "role": "ADMIN", "is_active": False, "is_mfa_verified": True}
    
    assert check_access(admin_mfa, "db", "DELETE") is True
    assert check_access(admin_no_mfa, "db", "DELETE") is False
    assert check_access(viewer, "db", "READ") is True
    assert check_access(viewer, "db", "WRITE") is False
    assert check_access(inactive, "db", "READ") is False
    print("  [PASS] Exercise 2: RBAC Access Checker works correctly!")

    # Test Exercise 3
    assert evaluate_password_security("12345") == "VERY WEAK"
    assert evaluate_password_security("Pass1234") == "MODERATE"
    assert evaluate_password_security("SuperSecurePass2026!#") == "STRONG"
    print("  [PASS] Exercise 3: Password Strength Evaluator works correctly!")

    print("\nAll Module 5 exercises passed successfully! Outstanding work!\n")

if __name__ == "__main__":
    run_tests()

