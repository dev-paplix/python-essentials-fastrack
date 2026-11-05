"""
Module 7: Loops and Functions - Student Practice Exercises
Course: Python Essentials FastTrack

Instructions:
1. Complete the challenges below using while loops, for loops, ternary operators,
   multi-dimensional arrays (1D, 2D, 3D), functions, and comprehensions.
2. Run this file to verify your solutions against the automated assertions.
"""

# =====================================================================
# Exercise 1: While Loop & Ternary Operator (Collatz Sequence Analyzer)
# =====================================================================
# Problem Statement:
# Write a function `collatz_sequence_analyzer(seed: int, max_steps: int = 1000) -> dict`
# The Collatz conjecture applies the following rule to a positive integer:
# - If current number n is even: next n is n // 2
# - If current number n is odd : next n is 3 * n + 1
# Requirements:
# 1. If seed <= 0, raise ValueError("Seed must be a positive integer.")
# 2. Use a `while` loop that continues while n != 1 and steps < max_steps.
# 3. Use the ternary operator to calculate the next value:
#    next_val = (n // 2) if n % 2 == 0 else (3 * n + 1)
# 4. Track all numbers in a sequence list, starting with `seed`.
# 5. Return a dictionary with:
#    {
#        "seed": int,
#        "steps": int (number of step transitions taken),
#        "peak_value": int (maximum number encountered in the sequence),
#        "sequence": list[int] (complete sequence starting from seed to the end),
#        "terminated": bool (True if n reached 1, False if max_steps was hit)
#    }

def collatz_sequence_analyzer(seed: int, max_steps: int = 1000) -> dict:
    """Analyze the Collatz sequence for a given seed using a while loop and ternary operator."""
    if seed <= 0:
        raise ValueError("Seed must be a positive integer.")
        
    sequence = [seed]
    current = seed
    steps = 0
    
    while current != 1 and steps < max_steps:
        # Use ternary conditional operator for next transition
        current = (current // 2) if current % 2 == 0 else (3 * current + 1)
        sequence.append(current)
        steps += 1
        
    return {
        "seed": seed,
        "steps": steps,
        "peak_value": max(sequence),
        "sequence": sequence,
        "terminated": current == 1
    }


# =====================================================================
# Exercise 2: 1D Array Traversal & Ternary Clamping
# =====================================================================
# Problem Statement:
# Write a function `categorize_and_clamp_1d(readings: list[float], min_val: float, max_val: float,
#                                         normal_low: float, normal_high: float) -> list[dict]`
# For each reading in `readings`:
# 1. Clamp the value between min_val and max_val using ternary expressions:
#    - If r < min_val: clamped = min_val
#    - Else if r > max_val: clamped = max_val
#    - Else: clamped = r
# 2. Categorize the reading status:
#    - "LOW" if reading < normal_low
#    - "HIGH" if reading > normal_high
#    - "NORMAL" otherwise
# 3. Return a list of dicts:
#    [
#       {"original": float (rounded 2 decimals), "clamped": float (rounded 2 decimals), "status": str},
#       ...
#    ]

def categorize_and_clamp_1d(readings: list[float], min_val: float, max_val: float,
                           normal_low: float, normal_high: float) -> list[dict]:
    """Iterates a 1D array, applying ternary clamping and status classification."""
    results = []
    for r in readings:
        clamped = min_val if r < min_val else (max_val if r > max_val else r)
        status = "LOW" if r < normal_low else ("HIGH" if r > normal_high else "NORMAL")
        results.append({
            "original": round(r, 2),
            "clamped": round(clamped, 2),
            "status": status
        })
    return results


# =====================================================================
# Exercise 3: 2D Array / Matrix Operations (Nested Loops)
# =====================================================================
# Problem Statement:
# Write a function `matrix_operations(matrix: list[list[int]]) -> dict`
# Given a rectangular 2D matrix (R rows, C columns):
# 1. Compute `row_sums`: list of sum of each row.
# 2. Compute `col_sums`: list of sum of each column across all rows.
# 3. Compute `diagonal_sum`: sum of elements on the primary diagonal (matrix[i][i] for i < min(R, C)).
# 4. Compute `flattened`: 1D list containing all elements of the matrix in row-major order.
# 5. Compute `parity_grid`: new 2D list of identical dimensions where each value is converted
#    to "EVEN" if even else "ODD" using the ternary operator.
# Return dict:
# {
#     "row_sums": list[int],
#     "col_sums": list[int],
#     "diagonal_sum": int,
#     "flattened": list[int],
#     "parity_grid": list[list[str]]
# }

def matrix_operations(matrix: list[list[int]]) -> dict:
    """Perform comprehensive 2D matrix calculations using nested loops."""
    if not matrix or not matrix[0]:
        return {
            "row_sums": [],
            "col_sums": [],
            "diagonal_sum": 0,
            "flattened": [],
            "parity_grid": []
        }
        
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # 1. Row sums
    row_sums = [sum(row) for row in matrix]
    
    # 2. Column sums using nested loops
    col_sums = []
    for c in range(num_cols):
        col_total = 0
        for r in range(num_rows):
            col_total += matrix[r][c]
        col_sums.append(col_total)
        
    # 3. Diagonal sum
    min_dim = min(num_rows, num_cols)
    diagonal_sum = sum(matrix[i][i] for i in range(min_dim))
    
    # 4. Flattened list via nested loop traversal
    flattened = []
    for row in matrix:
        for val in row:
            flattened.append(val)
            
    # 5. Parity grid using ternary expression
    parity_grid = []
    for row in matrix:
        parity_row = ["EVEN" if val % 2 == 0 else "ODD" for val in row]
        parity_grid.append(parity_row)
        
    return {
        "row_sums": row_sums,
        "col_sums": col_sums,
        "diagonal_sum": diagonal_sum,
        "flattened": flattened,
        "parity_grid": parity_grid
    }


# =====================================================================
# Exercise 4: 3D Array / Spatial Grid Processing (3-Level Nested Loops)
# =====================================================================
# Problem Statement:
# Write a function `analyze_3d_spatial_grid(datacube: list[list[list[float]]], alert_threshold: float) -> dict`
# Input: A 3D array indexed as datacube[layer][row][col] (e.g. Depth x Height x Width).
# Compute:
# 1. `layer_averages`: list of float averages for each layer (depth slice), rounded to 2 decimals.
# 2. `max_value`: float highest reading across the entire 3D volume.
# 3. `hotspot_coords`: list of (layer, row, col) tuples for all cells strictly > alert_threshold.
# 4. `total_volume_sum`: float sum of all values across all dimensions, rounded to 2 decimals.
# 5. `threshold_mask`: new 3D list matching datacube's shape, where each cell is 1 if cell > alert_threshold else 0
#    (using the ternary operator).
# Return dict matching the calculated keys above.

def analyze_3d_spatial_grid(datacube: list[list[list[float]]], alert_threshold: float) -> dict:
    """Analyze a 3-dimensional data volume using 3-level nested loops."""
    if not datacube:
        return {
            "layer_averages": [],
            "max_value": 0.0,
            "hotspot_coords": [],
            "total_volume_sum": 0.0,
            "threshold_mask": []
        }
        
    layer_averages = []
    hotspot_coords = []
    total_volume_sum = 0.0
    max_value = datacube[0][0][0]
    threshold_mask = []
    
    # 3-level nested loop traversal
    for layer_idx, layer in enumerate(datacube):
        layer_sum = 0.0
        layer_count = 0
        mask_layer = []
        
        for row_idx, row in enumerate(layer):
            mask_row = []
            for col_idx, val in enumerate(row):
                layer_sum += val
                layer_count += 1
                total_volume_sum += val
                
                if val > max_value:
                    max_value = val
                    
                if val > alert_threshold:
                    hotspot_coords.append((layer_idx, row_idx, col_idx))
                    
                # Ternary expression for mask
                mask_row.append(1 if val > alert_threshold else 0)
                
            mask_layer.append(mask_row)
            
        layer_avg = round(layer_sum / layer_count, 2) if layer_count > 0 else 0.0
        layer_averages.append(layer_avg)
        threshold_mask.append(mask_layer)
        
    return {
        "layer_averages": layer_averages,
        "max_value": round(max_value, 2),
        "hotspot_coords": hotspot_coords,
        "total_volume_sum": round(total_volume_sum, 2),
        "threshold_mask": threshold_mask
    }


# =====================================================================
# Exercise 5: Prime Number Range Generator (Loop-Else Pattern)
# =====================================================================
# Problem Statement:
# Write a function `generate_primes(start: int, end: int) -> list`
# Return a list of all prime numbers between `start` and `end` (inclusive).
# Use loop-else or helper functions. Note: numbers <= 1 are not prime.

def generate_primes(start: int, end: int) -> list:
    """Returns a list of prime numbers in the range [start, end] using loop-else."""
    primes = []
    for candidate in range(max(2, start), end + 1):
        # Check divisibility
        for divisor in range(2, int(candidate ** 0.5) + 1):
            if candidate % divisor == 0:
                break
        else:
            # Executes ONLY if inner loop did NOT break
            primes.append(candidate)
    return primes


# =====================================================================
# Exercise 6: Variadic Transaction Aggregator (*args, **kwargs)
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
# Exercise 7: Comprehension Refactoring
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
    print("=" * 65)
    print("RUNNING MODULE 7 PRACTICE TESTS")
    print("=" * 65)

    # Test Exercise 1: While Loop & Collatz Analyzer
    c_res = collatz_sequence_analyzer(6)
    assert c_res["seed"] == 6
    assert c_res["steps"] == 8
    assert c_res["peak_value"] == 16
    assert c_res["sequence"] == [6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert c_res["terminated"] is True

    # Test max_steps cutoff
    c_capped = collatz_sequence_analyzer(27, max_steps=10)
    assert c_capped["steps"] == 10
    assert c_capped["terminated"] is False

    # Test invalid seed
    try:
        collatz_sequence_analyzer(0)
        assert False, "Should raise ValueError for seed <= 0"
    except ValueError:
        pass
    print("  [PASS] Exercise 1: While Loop & Collatz Analyzer passed!")

    # Test Exercise 2: 1D Array Clamping & Ternary
    readings = [-10.0, 15.0, 25.5, 38.0, 55.0]
    res_1d = categorize_and_clamp_1d(readings, min_val=0.0, max_val=50.0, normal_low=18.0, normal_high=30.0)
    assert len(res_1d) == 5
    assert res_1d[0] == {"original": -10.0, "clamped": 0.0, "status": "LOW"}
    assert res_1d[1] == {"original": 15.0, "clamped": 15.0, "status": "LOW"}
    assert res_1d[2] == {"original": 25.5, "clamped": 25.5, "status": "NORMAL"}
    assert res_1d[3] == {"original": 38.0, "clamped": 38.0, "status": "HIGH"}
    assert res_1d[4] == {"original": 55.0, "clamped": 50.0, "status": "HIGH"}
    print("  [PASS] Exercise 2: 1D Array Traversal & Ternary Clamping passed!")

    # Test Exercise 3: 2D Matrix Operations
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    res_2d = matrix_operations(mat)
    assert res_2d["row_sums"] == [6, 15, 24]
    assert res_2d["col_sums"] == [12, 15, 18]
    assert res_2d["diagonal_sum"] == 15
    assert res_2d["flattened"] == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert res_2d["parity_grid"] == [
        ["ODD", "EVEN", "ODD"],
        ["EVEN", "ODD", "EVEN"],
        ["ODD", "EVEN", "ODD"]
    ]

    # Test Rectangular 2D Matrix (2x3)
    rect_mat = [
        [10, 20, 30],
        [40, 50, 60]
    ]
    res_rect = matrix_operations(rect_mat)
    assert res_rect["row_sums"] == [60, 150]
    assert res_rect["col_sums"] == [50, 70, 90]
    assert res_rect["diagonal_sum"] == 10 + 50
    print("  [PASS] Exercise 3: 2D Matrix Operations passed!")

    # Test Exercise 4: 3D Array Processing
    cube = [
        # Layer 0
        [
            [10.0, 20.0],
            [30.0, 40.0]
        ],
        # Layer 1
        [
            [50.0, 60.0],
            [70.0, 80.0]
        ]
    ]
    res_3d = analyze_3d_spatial_grid(cube, alert_threshold=55.0)
    assert res_3d["layer_averages"] == [25.0, 65.0]
    assert res_3d["max_value"] == 80.0
    assert res_3d["hotspot_coords"] == [(1, 0, 1), (1, 1, 0), (1, 1, 1)]
    assert res_3d["total_volume_sum"] == 360.0
    assert res_3d["threshold_mask"] == [
        [[0, 0], [0, 0]],
        [[0, 1], [1, 1]]
    ]
    print("  [PASS] Exercise 4: 3D Spatial Grid Processing passed!")

    # Test Exercise 5: Prime Generator
    primes_1_to_20 = generate_primes(1, 20)
    assert primes_1_to_20 == [2, 3, 5, 7, 11, 13, 17, 19], f"Got: {primes_1_to_20}"
    assert generate_primes(20, 28) == [23]
    print("  [PASS] Exercise 5: Prime Generator works correctly!")

    # Test Exercise 6: Financial Aggregator
    fin = aggregate_financials(500.0, -100.0, 300.0, -50.0, tax_rate=0.10, wire_fee=15.0, audit_fee=25.0)
    assert fin["gross_revenue"] == 800.0
    assert fin["gross_expenses"] == 150.0
    assert fin["tax_paid"] == 80.0
    assert fin["fees_total"] == 40.0
    assert fin["net_profit"] == 530.0
    print("  [PASS] Exercise 6: Financial Aggregator works correctly!")

    # Test Exercise 7: Dictionary Comprehension
    test_users = [
        {"id": 101, "username": "sarah", "active": True, "department": "Security"},
        {"id": 102, "username": "ken", "active": False, "department": "Security"},
        {"id": 103, "username": "elena", "active": True, "department": "Security"},
        {"id": 104, "username": "dave", "active": True, "department": "Billing"},
    ]
    sec_users = extract_active_department_users(test_users, "Security")
    assert sec_users == {101: "SARAH", 103: "ELENA"}
    print("  [PASS] Exercise 7: Dictionary Comprehension works correctly!")

    print("\nAll Module 7 exercises passed successfully! Outstanding work!\n")

if __name__ == "__main__":
    run_tests()
