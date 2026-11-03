"""
Module 7: Loops and Functions - Student Practice Exercises
Course: Python Essentials FastTrack

Instructions:
1. Complete the challenges below using loops, functions, and comprehensions.
2. Run this file to verify your solutions against the automated assertions.
"""

# =====================================================================
# Exercise 1: Prime Number Range Generator
# =====================================================================
# Problem Statement:
# Write a function `generate_primes(start: int, end: int) -> list`
# Return a list of all prime numbers between `start` and `end` (inclusive).
# Use loop-else or helper functions. Note: numbers <= 1 are not prime.

def generate_primes(start: int, end: int) -> list:
    """Returns a list of prime numbers in the range [start, end]."""
    primes = []
    for candidate in range(max(2, start), end + 1):
        # Check divisibility
        for divisor in range(2, int(candidate ** 0.5) + 1):
            if candidate % divisor == 0:
                break
        else:
            primes.append(candidate)
    return primes


# =====================================================================
# Exercise 2: Variadic Transaction Aggregator
# =====================================================================
# Problem Statement:
# Write a function `aggregate_financials(*transactions, tax_rate: float = 0.0, **category_fees) -> dict`
# - `transactions`: Variable number of float transaction amounts (e.g. 100.0, -25.0, 50.0).
#   Positive values are revenues, negative values are expenses.
# - `tax_rate`: Flat rate applied only to total revenue (default 0.0).
# - `**category_fees`: Arbitrary named fees to deduct from final net balance.
# Return a dict:
# {
#   "gross_revenue": float (sum of positives, rounded to 2 decimals),
#   "gross_expenses": float (absolute sum of negatives, rounded to 2 decimals),
#   "tax_paid": float (gross_revenue * tax_rate, rounded to 2 decimals),
#   "fees_total": float (sum of all kwargs values, rounded to 2 decimals),
#   "net_profit": float (gross_revenue - gross_expenses - tax_paid - fees_total, rounded to 2 decimals)
# }

def aggregate_financials(*transactions, tax_rate: float = 0.0, **category_fees) -> dict:
    """Aggregate financial transactions and deduct taxes and custom category fees."""
    revenues = sum(t for t in transactions if t > 0)
    expenses = abs(sum(t for t in transactions if t < 0))
    tax_paid = revenues * tax_rate
    fees_total = sum(category_fees.values())
    net_profit = revenues - expenses - tax_paid - fees_total
    
    return {
        "gross_revenue": round(revenues, 2),
        "gross_expenses": round(expenses, 2),
        "tax_paid": round(tax_paid, 2),
        "fees_total": round(fees_total, 2),
        "net_profit": round(net_profit, 2)
    }


# =====================================================================
# Exercise 3: Comprehension Refactoring
# =====================================================================
# Problem Statement:
# You are given a list of user dictionaries:
# users = [
#     {"id": 1, "username": "alice", "active": True, "department": "IT"},
#     {"id": 2, "username": "bob", "active": False, "department": "Sales"},
#     {"id": 3, "username": "charlie", "active": True, "department": "IT"},
# ]
# Write `extract_active_department_users(users: list, target_dept: str) -> dict`
# Using a SINGLE dictionary comprehension, return a dict mapping user ID to uppercase username
# for all ACTIVE users belonging to `target_dept`.
# E.g.: target_dept="IT" -> {1: "ALICE", 3: "CHARLIE"}

def extract_active_department_users(users: list, target_dept: str) -> dict:
    """Extract active users for a department using a dictionary comprehension."""
    return {
        u["id"]: u["username"].upper()
        for u in users
        if u.get("active") and u.get("department") == target_dept
    }


# =====================================================================
# Verification Test Suite
# =====================================================================
def run_tests():
    print("=" * 60)
    print("RUNNING MODULE 7 PRACTICE TESTS")
    print("=" * 60)

    # Test Exercise 1
    primes_1_to_20 = generate_primes(1, 20)
    assert primes_1_to_20 == [2, 3, 5, 7, 11, 13, 17, 19], f"Got: {primes_1_to_20}"
    assert generate_primes(20, 28) == [23]
    print("  [PASS] Exercise 1: Prime Generator works correctly!")

    # Test Exercise 2
    fin = aggregate_financials(500.0, -100.0, 300.0, -50.0, tax_rate=0.10, wire_fee=15.0, audit_fee=25.0)
    assert fin["gross_revenue"] == 800.0
    assert fin["gross_expenses"] == 150.0
    assert fin["tax_paid"] == 80.0
    assert fin["fees_total"] == 40.0
    # net = 800 - 150 - 80 - 40 = 530.0
    assert fin["net_profit"] == 530.0
    print("  [PASS] Exercise 2: Financial Aggregator works correctly!")

    # Test Exercise 3
    test_users = [
        {"id": 101, "username": "sarah", "active": True, "department": "Security"},
        {"id": 102, "username": "ken", "active": False, "department": "Security"},
        {"id": 103, "username": "elena", "active": True, "department": "Security"},
        {"id": 104, "username": "dave", "active": True, "department": "Billing"},
    ]
    sec_users = extract_active_department_users(test_users, "Security")
    assert sec_users == {101: "SARAH", 103: "ELENA"}
    print("  [PASS] Exercise 3: Dictionary Comprehension works correctly!")

    print("\nAll Module 7 exercises passed successfully! Outstanding work!\n")

if __name__ == "__main__":
    run_tests()

