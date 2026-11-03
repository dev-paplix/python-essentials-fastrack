"""
Module 5: Conditional Logic and Flow Control - Teaching Code
Instructor Demonstration Script
Course: Python Essentials FastTrack
"""

def header(title: str):
    print("\n" + "=" * 60)
    print(f" {title.upper()} ")
    print("=" * 60)

# =====================================================================
# 1. Comparison & Identity Mechanics
# =====================================================================
header("1. Equality (==) vs Identity (is)")

list_a = [10, 20, 30]
list_b = [10, 20, 30]
list_c = list_a

print(f"list_a == list_b (Values identical)  : {list_a == list_b}")
print(f"list_a is list_b (Different memory) : {list_a is list_b}")
print(f"list_a is list_c (Same memory alias): {list_a is list_c}")

# Sentinel comparisons
val = None
print(f"val is None: {val is None} (Always use 'is' for None, True, False)")

# =====================================================================
# 2. Short-Circuiting Mechanics
# =====================================================================
header("2. Short-Circuiting Evaluation")

def expensive_database_lookup():
    print("   [DB] Querying database... (expensive operation)")
    return True

print("Test 1: False and expensive_database_lookup()")
if False and expensive_database_lookup():
    pass
print("   -> Notice database lookup was NEVER called!")

print("\nTest 2: True or expensive_database_lookup()")
if True or expensive_database_lookup():
    pass
print("   -> Notice database lookup was NEVER called!")

# Guarding division by zero with short-circuiting:
divisor = 0
result = (divisor != 0) and (100 / divisor > 5)
print(f"\nSafe zero-division guard returned: {result}")

# =====================================================================
# 3. Guard Clauses & Flow Architecture
# =====================================================================
header("3. Refactoring Nested Conditions with Guard Clauses")

def evaluate_loan_application(applicant: dict) -> str:
    """
    Evaluates loan eligibility using clean guard clauses.
    applicant format: {'age': int, 'income': float, 'credit_score': int, 'bankrupt': bool}
    """
    if applicant.get("age", 0) < 21:
        return "REJECTED: Minimum age requirement is 21"
    
    if applicant.get("bankrupt", False):
        return "REJECTED: Active bankruptcy record on file"
        
    if applicant.get("credit_score", 0) < 650:
        return "REJECTED: Credit score below 650 threshold"
        
    if applicant.get("income", 0) < 35_000:
        return "REJECTED: Annual income below $35,000 threshold"
        
    return "APPROVED: Qualified for standard loan issuance"

app_1 = {"age": 19, "income": 50000, "credit_score": 720, "bankrupt": False}
app_2 = {"age": 30, "income": 40000, "credit_score": 620, "bankrupt": False}
app_3 = {"age": 35, "income": 85000, "credit_score": 750, "bankrupt": False}

print(f"Applicant 1: {evaluate_loan_application(app_1)}")
print(f"Applicant 2: {evaluate_loan_application(app_2)}")
print(f"Applicant 3: {evaluate_loan_application(app_3)}")

# =====================================================================
# 4. Ternary Conditional Operator
# =====================================================================
header("4. Ternary Conditional Expressions")

account_balance = 250.0
transaction_fee = 0.0 if account_balance >= 500.0 else 12.50
print(f"Balance: ${account_balance:.2f} -> Fee Applied: ${transaction_fee:.2f}")

if __name__ == "__main__":
    print("\n[SUCCESS] Module 5 Teaching Code executed successfully!")

