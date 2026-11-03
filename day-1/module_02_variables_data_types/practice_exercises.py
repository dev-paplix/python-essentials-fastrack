"""
=============================================================================
Course   : Python Essentials [FastTrack] - Day 1
Module   : Module 2 - Core Concepts: Variables and Data Types
Audience : Absolute Beginners
Topic    : Student Hands-On Practice Exercises
=============================================================================

RULES FOR MODULE 2 EXERCISES:
- Only use variables, type casting (int, float, str, bool), and operators.
- NO functions (def) required.
- NO if / else statements required.
- NO loops (for / while) required.
=============================================================================
"""

print("=" * 70)
print("MODULE 2: HANDS-ON PRACTICE EXERCISES FOR STUDENTS")
print("=" * 70)

# ===========================================================================
# EXERCISE 1: DATA TYPE DETECTIVE (INSPECTING TYPES)
# ===========================================================================
# Goal: Assign 5 different values to variables and print their types with type().
#
# Requirements:
# 1. var_a = 2026
# 2. var_b = 36.6
# 3. var_c = "Python FastTrack"
# 4. var_d = True
# 5. var_e = None
# Print each variable and its corresponding type().
# ===========================================================================
print("\n--- EXERCISE 1: DATA TYPE DETECTIVE ---")

var_a = 2026
var_b = 36.6
var_c = "Python FastTrack"
var_d = True
var_e = None

print("var_a :", var_a, "| Type :", type(var_a))
print("var_b :", var_b, "| Type :", type(var_b))
print("var_c :", var_c, "| Type :", type(var_c))
print("var_d :", var_d, "| Type :", type(var_d))
print("var_e :", var_e, "| Type :", type(var_e))


# ===========================================================================
# EXERCISE 2: WEB FORM DATA SANITIZER (EXPLICIT CASTING)
# ===========================================================================
# Goal: Convert string data from a web form into appropriate numeric types
# and perform calculations.
#
# Scenario:
# You receive the following string variables from a form:
# str_weight = "68.5"   (weight in kilograms)
# str_height = "1.75"   (height in meters)
#
# Task:
# 1. Convert str_weight to a float.
# 2. Convert str_height to a float.
# 3. Calculate BMI (Body Mass Index) formula: BMI = weight / (height * height)
# 4. Print the result.
# ===========================================================================
print("\n--- EXERCISE 2: WEB FORM NUMERIC CONVERSION ---")

str_weight = "68.5"
str_height = "1.75"

# Convert to float
weight_kg = float(str_weight)
height_m = float(str_height)

# Calculate BMI
bmi = weight_kg / (height_m * height_m)

print("Weight (kg) :", weight_kg)
print("Height (m)  :", height_m)
print("BMI Score   :", bmi)


# ===========================================================================
# EXERCISE 3: PYTHONIC VARIABLE SWAP
# ===========================================================================
# Goal: Swap the contents of two variables in a single line without temporary variables.
#
# Scenario:
# Cup A has "Coffee".
# Cup B has "Tea".
# Swap them so Cup A has "Tea" and Cup B has "Coffee".
# ===========================================================================
print("\n--- EXERCISE 3: VARIABLE SWAPPING ---")

cup_a = "Coffee"
cup_b = "Tea"

print("Before Swap: Cup A =", cup_a, "| Cup B =", cup_b)

# Pythonic swap in one single line:
cup_a, cup_b = cup_b, cup_a

print("After Swap : Cup A =", cup_a, "| Cup B =", cup_b)


# ===========================================================================
# EXERCISE 4: AUGMENTED ASSIGNMENT GAME INVENTORY
# ===========================================================================
# Goal: Track a player's gold coins and health points using +=, -=, *=, /=.
#
# Scenario:
# Player starts with:
# - gold = 100
# - health = 100
#
# Sequence of events:
# 1. Player defeats a monster: gains 45 gold. (Use +=)
# 2. Player takes damage from a trap: loses 20 health. (Use -=)
# 3. Player opens a double-wealth treasure chest: doubles their gold. (Use *=)
# 4. Player drinks a recovery potion: health resets by +15. (Use +=)
# Print final gold and health.
# ===========================================================================
print("\n--- EXERCISE 4: AUGMENTED ASSIGNMENT INVENTORY ---")

player_gold = 100
player_health = 100
print("Initial Stats  -> Gold:", player_gold, "| Health:", player_health)

# 1. Monster defeated (+45 gold)
player_gold += 45

# 2. Trap damage (-20 health)
player_health -= 20

# 3. Double wealth (*= 2 gold)
player_gold *= 2

# 4. Potion (+15 health)
player_health += 15

print("Final Stats    -> Gold:", player_gold, "| Health:", player_health)


# ===========================================================================
# EXERCISE 5: TRUTHY / FALSY EXPERIMENT
# ===========================================================================
# Goal: Experiment with bool() conversion on different variable values.
#
# Task:
# Create 4 variables and print their boolean truthiness:
# 1. username = "" (empty string)
# 2. registered_user = "Alice" (non-empty string)
# 3. shopping_cart_items = 0
# 4. discount_voucher = 15
# ===========================================================================
print("\n--- EXERCISE 5: TRUTHY & FALSY CONVERSIONS ---")

username = ""
registered_user = "Alice"
shopping_cart_items = 0
discount_voucher = 15

print("Empty username '' truthiness          :", bool(username))
print("Registered user 'Alice' truthiness    :", bool(registered_user))
print("Zero cart items 0 truthiness          :", bool(shopping_cart_items))
print("Discount voucher 15 truthiness        :", bool(discount_voucher))

print("\n" + "=" * 70)
print("[SUCCESS] All Module 2 Practice Exercises Completed Successfully!")
print("=" * 70)
