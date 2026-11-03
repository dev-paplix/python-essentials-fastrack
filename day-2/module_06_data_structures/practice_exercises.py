"""
Module 6: Data Structures in Python - Student Practice Exercises
Course: Python Essentials FastTrack

Instructions:
1. Implement the exercises below using lists, dictionaries, and copy mechanisms.
2. Run this file to verify your solutions against the automated assertions.
"""

import copy

# =====================================================================
# Exercise 1: In-Memory Inventory Manager
# =====================================================================
# Problem Statement:
# Implement an inventory dictionary manager with functions:
# - `add_stock(inventory: dict, sku: str, name: str, qty: int, price: float)`
#   If sku already exists, increment qty and update price; otherwise insert new entry.
# - `sell_stock(inventory: dict, sku: str, qty: int) -> bool`
#   If sku exists and inventory[sku]["qty"] >= qty, decrement and return True.
#   Otherwise return False.
# - `calculate_total_value(inventory: dict) -> float`
#   Returns the sum of (qty * price) for all products, rounded to 2 decimal places.

def add_stock(inventory: dict, sku: str, name: str, qty: int, price: float):
    """Add or restock an inventory product."""
    if sku in inventory:
        inventory[sku]["qty"] += qty
        inventory[sku]["price"] = price
    else:
        inventory[sku] = {
            "name": name,
            "qty": qty,
            "price": price
        }

def sell_stock(inventory: dict, sku: str, qty: int) -> bool:
    """Process a sale if sufficient stock is present."""
    if sku not in inventory or inventory[sku]["qty"] < qty:
        return False
    inventory[sku]["qty"] -= qty
    return True

def calculate_total_value(inventory: dict) -> float:
    """Calculate the total wholesale valuation of all items in stock."""
    total = sum(item["qty"] * item["price"] for item in inventory.values())
    return round(total, 2)


# =====================================================================
# Exercise 2: Student Gradebook Statistics
# =====================================================================
# Problem Statement:
# Given a dictionary where keys are student names and values are lists of exam scores:
# e.g., {"Alice": [80, 90, 85], "Bob": [70, 75, 72]}
# Write `compute_grade_averages(gradebook: dict) -> dict`
# Return a dict mapping each student name to their average score (rounded to 1 decimal place),
# AND sort the resulting dict so the highest-scoring student appears first!

def compute_grade_averages(gradebook: dict) -> dict:
    """Computes average score per student and returns sorted dict (descending)."""
    averages = {}
    for student, scores in gradebook.items():
        avg = sum(scores) / len(scores) if scores else 0.0
        averages[student] = round(avg, 1)
        
    # Sort by average descending
    sorted_items = sorted(averages.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items)


# =====================================================================
# Exercise 3: Matrix Column Extractor
# =====================================================================
# Problem Statement:
# Given a 2D list (matrix) of integers, write `extract_column(matrix: list, col_idx: int) -> list`
# Return a list containing all elements at column index `col_idx`.
# E.g.: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], col_idx = 1 -> [2, 5, 8]

def extract_column(matrix: list, col_idx: int) -> list:
    """Extract a single vertical column from a 2D matrix list."""
    return [row[col_idx] for row in matrix]


# =====================================================================
# Verification Test Suite
# =====================================================================
def run_tests():
    print("=" * 60)
    print("RUNNING MODULE 6 PRACTICE TESTS")
    print("=" * 60)

    # Test Exercise 1
    inventory = {}
    add_stock(inventory, "SKU-1", "Laptop", 10, 1200.0)
    add_stock(inventory, "SKU-2", "Mouse", 50, 25.0)
    assert calculate_total_value(inventory) == (10 * 1200.0) + (50 * 25.0) # 12000 + 1250 = 13250.0

    assert sell_stock(inventory, "SKU-1", 3) is True
    assert inventory["SKU-1"]["qty"] == 7
    assert sell_stock(inventory, "SKU-1", 10) is False # Insufficient stock
    assert inventory["SKU-1"]["qty"] == 7
    print("  [PASS] Exercise 1: Inventory Manager works correctly!")

    # Test Exercise 2
    grades = {
        "Bob": [70, 75, 80],       # avg = 75.0
        "Alice": [90, 95, 94],     # avg = 93.0
        "Charlie": [85, 88, 82],   # avg = 85.0
    }
    ranked = compute_grade_averages(grades)
    keys_order = list(ranked.keys())
    assert keys_order == ["Alice", "Charlie", "Bob"], f"Unexpected order: {keys_order}"
    assert ranked["Alice"] == 93.0
    assert ranked["Bob"] == 75.0
    print("  [PASS] Exercise 2: Gradebook Ranking works correctly!")

    # Test Exercise 3
    matrix = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    col0 = extract_column(matrix, 0)
    col1 = extract_column(matrix, 1)
    assert col0 == [10, 40, 70]
    assert col1 == [20, 50, 80]
    print("  [PASS] Exercise 3: Matrix Column Extractor works correctly!")

    print("\nAll Module 6 exercises passed successfully! Outstanding work!\n")

if __name__ == "__main__":
    run_tests()

