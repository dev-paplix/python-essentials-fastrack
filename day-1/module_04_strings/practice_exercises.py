"""
=============================================================================
Course   : Python Essentials [FastTrack] - Day 1
Module   : Module 4 - String Manipulation
Audience : Absolute Beginners
Topic    : Student Hands-On Practice Exercises
=============================================================================

RULES FOR MODULE 4 EXERCISES:
- Only use string indexing, slicing, methods, and f-strings.
- NO functions (def) required.
- NO if / else statements required.
- NO loops (for / while) required.
=============================================================================
"""

print("=" * 70)
print("MODULE 4: HANDS-ON PRACTICE EXERCISES FOR STUDENTS")
print("=" * 70)

# ===========================================================================
# EXERCISE 1: SLICING AND EXTRACTION
# ===========================================================================
# Goal: Extract specific parts of a string using slicing.
#
# Given:
# transaction_id = "TXN-2026-KL-987654"
#
# Tasks:
# 1. Extract prefix "TXN" (first 3 characters).
# 2. Extract year "2026".
# 3. Extract city code "KL".
# 4. Extract account number "987654" (last 6 characters using negative index).
# ===========================================================================
print("\n--- EXERCISE 1: SLICING AND EXTRACTION ---")

transaction_id = "TXN-2026-KL-987654"

prefix = transaction_id[0:3]
year = transaction_id[4:8]
city_code = transaction_id[9:11]
account_num = transaction_id[-6:]

print("Original Transaction ID :", transaction_id)
print("Prefix                  :", prefix)
print("Year                    :", year)
print("City Code               :", city_code)
print("Account Number          :", account_num)


# ===========================================================================
# EXERCISE 2: DATA HYGIENE (CLEANING MESSY USER INPUT)
# ===========================================================================
# Goal: Clean and normalize user contact information.
#
# Given:
# dirty_name = "   sItI nUrHALIZA   "
# dirty_phone = "   012 345 6789   "
#
# Tasks:
# 1. Strip spaces and title-case dirty_name.
# 2. Strip spaces and replace spaces with hyphens in dirty_phone so it looks like: "012-345-6789".
# ===========================================================================
print("\n--- EXERCISE 2: DATA HYGIENE ---")

dirty_name = "   sItI nUrHALIZA   "
dirty_phone = "   012 345 6789   "

clean_name = dirty_name.strip().title()
clean_phone = dirty_phone.strip().replace(" ", "-")

print("Clean Name  :", clean_name)
print("Clean Phone :", clean_phone)


# ===========================================================================
# EXERCISE 3: EMAIL PARSER (SPLITTING)
# ===========================================================================
# Goal: Use .split() to parse an email address.
#
# Given:
# employee_email = "devops.lead@gemrain.net"
#
# Tasks:
# 1. Split the email by "@" to get the username and the domain.
# 2. Split the username by "." to get the first title and second title.
# 3. Print the results using an f-string.
# ===========================================================================
print("\n--- EXERCISE 3: EMAIL PARSER ---")

employee_email = "devops.lead@gemrain.net"

# Split by "@"
parts = employee_email.split("@")
username = parts[0]
domain = parts[1]

# Split username by "."
user_tokens = username.split(".")
role_title = user_tokens[0].title()
seniority = user_tokens[1].title()

print(f"Full Email : {employee_email}")
print(f"Username   : {username}")
print(f"Domain     : {domain}")
print(f"Role Title : {role_title} {seniority}")


# ===========================================================================
# EXERCISE 4: SENSITIVE DATA MASKER
# ===========================================================================
# Goal: Mask a Malaysian NRIC (Identity Card) number.
#
# Given:
# nric = "981215-14-5544"
# A standard format is: birthdate(6 digits) - state(2 digits) - random(4 digits).
# For privacy, mask all characters except the first 6 birthdate digits!
# Result should look like: "981215-**-****"
# ===========================================================================
print("\n--- EXERCISE 4: NRIC SENSITIVE DATA MASKER ---")

nric = "981215-14-5544"

# Extract birthdate portion: first 6 digits
birthdate_part = nric[:6]
masked_nric = birthdate_part + "-**-****"

print("Original NRIC :", nric)
print("Masked NRIC   :", masked_nric)


# ===========================================================================
# EXERCISE 5: FORMATTED RECEIPT GENERATOR USING F-STRINGS
# ===========================================================================
# Goal: Build an aligned terminal receipt using modern f-strings.
#
# Given:
# item_name = "Cloud Database Subscription"
# unit_price = 1450.75
# months = 6
#
# Tasks:
# 1. Calculate total = unit_price * months
# 2. Print a formatted box with:
#    - Left aligned item name
#    - Right aligned unit price with 2 decimals
#    - Right aligned total with comma and 2 decimals
# ===========================================================================
print("\n--- EXERCISE 5: FORMATTED RECEIPT ---")

item_name = "Cloud Database Subscription"
unit_price = 1450.75
months = 6
total_cost = unit_price * months

print("+" + "-" * 50 + "+")
print(f"| {'INVOICE STATEMENT':^48} |")
print("+" + "-" * 50 + "+")
print(f"| Item  : {item_name:<38} |")
print(f"| Rate  : RM {unit_price:>10.2f} / month{' ':<16} |")
print(f"| Period: {months:>2} months{' ':<31} |")
print("+" + "-" * 50 + "+")
print(f"| TOTAL : RM {total_cost:>10,.2f}{' ':<24} |")
print("+" + "-" * 50 + "+")

print("\n" + "=" * 70)
print("[SUCCESS] All Module 4 Practice Exercises Completed Successfully!")
print("=" * 70)
