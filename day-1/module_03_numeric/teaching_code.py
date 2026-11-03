"""
=============================================================================
Course   : Python Essentials [FastTrack] - Day 1
Module   : Module 3 - Numeric in Python
Audience : Absolute Beginners
Topic    : Instructor Teaching Code & Live Demonstration Script
=============================================================================

PEDAGOGICAL RULE FOR MODULE 3:
- Builds strictly upon Modules 1 and 2.
- Explores numbers, arithmetic operators, precedence, math module.
- NO functions (def) - that is Module 7!
- NO conditionals (if / else) - that is Module 5!
- NO loops (for / while) - that is Module 7!
- Pure, sequential, step-by-step beginner code.
=============================================================================
"""

import math
from decimal import Decimal

# ===========================================================================
# SECTION 1: THE TWO MAIN NUMERIC TYPES (int vs float)
# ===========================================================================
print("=" * 70)
print("SECTION 1: INTEGERS AND FLOATS")
print("=" * 70)

# Integers are whole numbers:
total_students = 28
days_in_year = 365
bank_balance_cents = 150000

# Floats are numbers with decimal points:
gpa = 3.85
tax_rate = 0.06
fuel_price = 2.05

print("Integer value :", total_students, "| Type :", type(total_students))
print("Float value   :", gpa, "| Type :", type(gpa))

# Special feature of Python Integers: ARBITRARY PRECISION
# Unlike other languages where integers overflow at 2 billion,
# Python integers can grow to thousands of digits without breaking!
huge_number = 2 ** 100
print("\n2 to the power of 100 is:")
print(huge_number)
print("Number of digits in this huge number:", len(str(huge_number)))


# ===========================================================================
# SECTION 2: THE 7 ARITHMETIC OPERATORS
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 2: THE 7 ARITHMETIC OPERATORS IN PYTHON")
print("=" * 70)

num1 = 17
num2 = 5

print("Operating on num1 =", num1, "and num2 =", num2)
print("1. Addition         (+)  :", num1 + num2)   # 22
print("2. Subtraction      (-)  :", num1 - num2)   # 12
print("3. Multiplication   (*)  :", num1 * num2)   # 85
print("4. True Division    (/)  :", num1 / num2)   # 3.4 (Always returns float!)
print("5. Floor Division   (//) :", num1 // num2)  # 3 (Discards the decimal part)
print("6. Modulo/Remainder (%)  :", num1 % num2)   # 2 (17 divided by 5 is 3 with remainder 2)
print("7. Exponentiation   (**) :", num1 ** 2)      # 289 (17 squared)


# ===========================================================================
# SECTION 3: FLOOR DIVISION (//) AND MODULO (%) IN DEPTH
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 3: DEEP DIVE INTO FLOOR DIVISION AND MODULO")
print("=" * 70)

# Real-world problem: Egg packaging
# You have 38 eggs. Each carton holds 12 eggs.
# How many full cartons do you have, and how many eggs are left over?
total_eggs = 38
carton_capacity = 12

full_cartons = total_eggs // carton_capacity  # Floor division gives full cartons
leftover_eggs = total_eggs % carton_capacity   # Modulo gives leftover eggs

print("Total Eggs       :", total_eggs)
print("Full Cartons     :", full_cartons)
print("Leftover Eggs    :", leftover_eggs)

# Real-world problem: Converting Seconds to Minutes and Seconds
# 195 seconds total:
total_seconds = 195
minutes = total_seconds // 60
seconds = total_seconds % 60
print("\n195 seconds =", minutes, "minutes and", seconds, "seconds")


# ===========================================================================
# SECTION 4: ORDER OF OPERATIONS (PEMDAS / BODMAS)
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 4: ORDER OF OPERATIONS (PEMDAS)")
print("=" * 70)

# PEMDAS:
# P : Parentheses ()
# E : Exponents **
# M : Multiplication *
# D : Division / and // and %
# A : Addition +
# S : Subtraction -

# Example 1: Without parentheses (Multiplication happens FIRST!)
result_1 = 10 + 5 * 2
print("10 + 5 * 2 =", result_1) # 20 (not 30!)

# Example 2: With parentheses (Parentheses happen FIRST!)
result_2 = (10 + 5) * 2
print("(10 + 5) * 2 =", result_2) # 30

# Example 3: Exponents happen before multiplication
result_3 = 3 * 2 ** 3
print("3 * 2 ** 3 =", result_3) # 3 * 8 = 24


# ===========================================================================
# SECTION 5: THE FLOATING-POINT PRECISION QUIRK
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 5: WHY 0.1 + 0.2 IS NOT 0.3 IN COMPUTERS")
print("=" * 70)

# Computers think in base-2 (binary 0 and 1).
# Fractions like 1/10 (0.1) cannot be represented exactly in binary,
# just like 1/3 (0.3333...) cannot be represented cleanly in decimal.
quirk_result = 0.1 + 0.2
print("0.1 + 0.2 in Python looks like :", quirk_result)
print("Is 0.1 + 0.2 == 0.3?           :", quirk_result == 0.3)

# Solution 1: Use round() for general display
print("round(0.1 + 0.2, 2)            :", round(quirk_result, 2))

# Solution 2: For banking and financial applications, use Decimal!
dec1 = Decimal("0.1")
dec2 = Decimal("0.2")
dec_sum = dec1 + dec2
print("Using Decimal('0.1') + Decimal('0.2'):", dec_sum)
print("Is dec_sum == Decimal('0.3')?        :", dec_sum == Decimal("0.3"))


# ===========================================================================
# SECTION 6: THE BUILT-IN math MODULE
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 6: EXPLORING PYTHON'S math MODULE")
print("=" * 70)

# Python comes with a built-in library called 'math'.
# To use it, we write: import math

print("Value of Pi (math.pi)              :", math.pi)
print("Value of Euler's number (math.e)   :", math.e)

# Square root: math.sqrt()
print("Square root of 64 (math.sqrt(64))  :", math.sqrt(64))
print("Square root of 2  (math.sqrt(2))   :", round(math.sqrt(2), 4))

# Rounding UP vs Rounding DOWN:
# math.ceil() always rounds UP to the nearest integer
# math.floor() always rounds DOWN to the nearest integer
original_val = 4.15
print("Value                              :", original_val)
print("math.ceil(4.15)  (Rounds UP)       :", math.ceil(original_val))
print("math.floor(4.15) (Rounds DOWN)     :", math.floor(original_val))

# Factorial: 5! = 5 * 4 * 3 * 2 * 1
print("math.factorial(5)                  :", math.factorial(5))


# ===========================================================================
# SECTION 7: PROJECT - COMPOUND INTEREST & LOAN CALCULATOR
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 7: PROJECT - FINANCIAL COMPOUND INTEREST CALCULATION")
print("=" * 70)

# Financial Formula:
# Future Value = Principal * (1 + annual_rate / compounding_periods) ** (compounding_periods * years)
initial_deposit = 10000.00   # RM 10,000 initial investment
annual_rate = 0.05           # 5% annual return
compounding_per_year = 12    # Compounded monthly
investment_years = 5         # 5 years

# Step 1: Calculate the growth factor
rate_per_period = annual_rate / compounding_per_year
total_periods = compounding_per_year * investment_years
growth_factor = (1 + rate_per_period) ** total_periods

# Step 2: Calculate future value
final_balance = initial_deposit * growth_factor
total_interest_earned = final_balance - initial_deposit

print("Initial Investment    : RM", initial_deposit)
print("Annual Interest Rate  :", annual_rate * 100, "%")
print("Investment Period     :", investment_years, "years")
print("Compounding Frequency : Monthly (12 times/year)")
print("-" * 45)
print("Final Balance         : RM", round(final_balance, 2))
print("Total Interest Earned : RM", round(total_interest_earned, 2))
print("-" * 45)
print("Module 3 Teaching Code finished successfully!")
