"""
=============================================================================
Course   : Python Essentials [FastTrack] - Day 1
Module   : Module 1 - Introduction to Python
Audience : Absolute Beginners (No prior programming experience required)
Topic    : Student Hands-On Practice Exercises
=============================================================================

RULES FOR MODULE 1 EXERCISES:
- Only use print(), variables, basic math (+, -, *, /), and string concatenation.
- NO functions (def) required.
- NO if / else statements required.
- NO loops (for / while) required.
=============================================================================
"""

print("=" * 70)
print("MODULE 1: HANDS-ON PRACTICE EXERCISES FOR STUDENTS")
print("=" * 70)

# ===========================================================================
# EXERCISE 1: THE WELCOME CARD (PRINTING & BORDERS)
# ===========================================================================
# Goal: Use print() statements to display an attractive welcome banner
# for a new employee joining your company.
#
# Requirements:
# 1. Print a top and bottom border using 50 asterisks (*) or equal signs (=).
# 2. Print a centered welcome message.
# 3. Print the employee's name, role, and starting date.
# ===========================================================================
print("\n--- EXERCISE 1: WELCOME CARD ---")

# Step 1: Define the variables
new_hire_name = "Nurul Huda"
new_hire_role = "Junior Python Developer"
start_date = "01-December-2026"

# Step 2: Print the banner (Students practice borders and layout)
print("*" * 50)
print("          WELCOME TO GEMRAIN CONSULTING           ")
print("*" * 50)
print("Employee Name :", new_hire_name)
print("Position      :", new_hire_role)
print("Start Date    :", start_date)
print("*" * 50)


# ===========================================================================
# EXERCISE 2: PRINT FORMATTING WITH sep= AND end=
# ===========================================================================
# Goal: Practice using the 'sep' and 'end' parameters of the print() function.
#
# Requirements:
# 1. Print a date formatted as: 2026/11/03 using sep="/"
# 2. Print an IP address formatted as: 192.168.1.100 using sep="."
# 3. Print the words: "Downloading", "file", "now" on the SAME LINE using end="... "
# ===========================================================================
print("\n--- EXERCISE 2: sep= AND end= CUSTOMIZATIONS ---")

# Task 2.1: Date with slash separator
year = "2026"
month = "11"
day = "03"
print("Formatted Date : ", end="")
print(year, month, day, sep="/")

# Task 2.2: IP Address with dot separator
ip_part1 = 192
ip_part2 = 168
ip_part3 = 1
ip_part4 = 100
print("Server IP      : ", end="")
print(ip_part1, ip_part2, ip_part3, ip_part4, sep=".")

# Task 2.3: Same line printing with end
print("Progress       : ", end="")
print("Connecting", end=" -> ")
print("Authenticating", end=" -> ")
print("Connected!", end="\n")


# ===========================================================================
# EXERCISE 3: SEQUENTIAL INPUT-PROCESS-OUTPUT (IPO) - RESTAURANT BILL
# ===========================================================================
# Goal: Build a sequential restaurant bill splitter without using functions or ifs.
#
# Scenario:
# 4 colleagues have lunch together.
# Total food bill is RM 160.00.
# Service tax is 6% (0.06).
# Service charge tip is 10% (0.10).
# Calculate:
# - Tax amount
# - Tip amount
# - Final grand total
# - Share per person (Grand Total divided by 4)
# ===========================================================================
print("\n--- EXERCISE 3: RESTAURANT BILL SPLITTER (IPO MODEL) ---")

# 1. INPUT (Data given)
food_bill = 160.00
tax_rate = 0.06
tip_rate = 0.10
number_of_diners = 4

# 2. PROCESS (Calculations)
tax_amount = food_bill * tax_rate
tip_amount = food_bill * tip_rate
grand_total = food_bill + tax_amount + tip_amount
share_per_diner = grand_total / number_of_diners

# 3. OUTPUT (Display results cleanly)
print("Food Subtotal    : RM", food_bill)
print("Service Tax (6%) : RM", tax_amount)
print("Tip (10%)        : RM", tip_amount)
print("-" * 35)
print("Grand Total      : RM", grand_total)
print("Share Per Person : RM", share_per_diner)
print("-" * 35)


# ===========================================================================
# EXERCISE 4: THE MAD LIBS STORY GENERATOR
# ===========================================================================
# Goal: Create a dynamic funny story by substituting variables into strings.
#
# Requirements:
# 1. Store variables: hero_name, pet_animal, vehicle, city, snack.
# 2. Print a 4-line mini story using those variables.
# ===========================================================================
print("\n--- EXERCISE 4: STORY GENERATOR ---")

hero_name = "Alex"
pet_animal = "golden retriever"
vehicle = "electric scooter"
city = "Kuala Lumpur"
snack = "curry puffs"

print("Once upon a time in " + city + ", " + hero_name + " was riding a " + vehicle + ".")
print("Right beside " + hero_name + " was a loyal " + pet_animal + " wearing sunglasses.")
print("They were on an urgent secret mission to find the best " + snack + " in town.")
print("Mission accomplished: the " + snack + " was delicious!")


# ===========================================================================
# EXERCISE 5: DEBUGGING CHALLENGE (SPOT AND EXPLAIN THE ERRORS)
# ===========================================================================
# Below are 5 common mistakes beginners make.
# In this exercise, read through each line, understand why the commented
# line failed, and see the corrected version below it!
# ===========================================================================
print("\n--- EXERCISE 5: DEBUGGING CODE PRACTICE ---")

# Bug 1: Case Sensitivity
# BROKEN : Print("Python is awesome")
# REASON : Python is case sensitive; 'Print' with a capital 'P' is not recognized.
# FIXED  :
print("Bug 1 Fixed : Python is case sensitive, always use lowercase 'print()'!")

# Bug 2: Missing quotation marks around text
# BROKEN : print(Welcome to Malaysia)
# REASON : Without quotes, Python thinks 'Welcome', 'to', 'Malaysia' are variables.
# FIXED  :
print("Bug 2 Fixed : Text must always be wrapped in quotes: 'Welcome to Malaysia'")

# Bug 3: Mismatched quotes
# BROKEN : print("Hello World')
# REASON : Starts with a double quote (") but ends with a single quote (').
# FIXED  :
print("Bug 3 Fixed : Opening and closing quotes must match!")

# Bug 4: Treating numbers as strings when you want to do math
# BROKEN : total = "20" + "30"  (this gives "2030", not 50!)
# REASON : Putting quotes around numbers makes them text.
# FIXED  :
math_total = 20 + 30
print("Bug 4 Fixed : 20 + 30 without quotes equals:", math_total)

# Bug 5: Missing comma between print arguments
# BROKEN : print("Your total is:" 100)
# REASON : Separate arguments must have a comma between them.
# FIXED  :
print("Bug 5 Fixed : Your total is:", 100)

print("\n" + "=" * 70)
print("[SUCCESS] All Module 1 Practice Exercises Completed Successfully!")
print("=" * 70)
