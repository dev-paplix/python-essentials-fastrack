"""
=============================================================================
Course   : Python Essentials [FastTrack] - Day 1
Module   : Module 4 - String Manipulation
Audience : Absolute Beginners
Topic    : Instructor Teaching Code & Live Demonstration Script
=============================================================================

PEDAGOGICAL RULE FOR MODULE 4:
- Builds strictly upon Modules 1, 2, and 3.
- Explores string indexing, slicing, methods, and f-strings.
- NO functions (def) - that is Module 7!
- NO conditionals (if / else) - that is Module 5!
- NO loops (for / while) - that is Module 7!
- Pure, sequential, step-by-step beginner code.
=============================================================================
"""

# ===========================================================================
# SECTION 1: STRING INDEXING (ZERO-BASED & NEGATIVE)
# ===========================================================================
print("=" * 70)
print("SECTION 1: STRING INDEXING (READING INDIVIDUAL CHARACTERS)")
print("=" * 70)

# In Python, each character has an index position starting at 0:
# Index:      0   1   2   3   4   5
# Character:  P   y   t   h   o   n
# Negative:  -6  -5  -4  -3  -2  -1

course_name = "Python"

print("Original string :", course_name)
print("Length (len())  :", len(course_name), "characters")

# Positive Indexing (from the left):
print("\nPositive Indexing:")
print("First character [0] :", course_name[0])  # P
print("Second character [1]:", course_name[1])  # y
print("Third character [2] :", course_name[2])  # t

# Negative Indexing (from the right/end):
print("\nNegative Indexing (counting backwards):")
print("Last character [-1] :", course_name[-1])  # n
print("Second last [-2]    :", course_name[-2])  # o


# ===========================================================================
# SECTION 2: STRING SLICING ([start : stop : step])
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 2: STRING SLICING (EXTRACTING SUBSTRINGS)")
print("=" * 70)

# Syntax: string[start : stop : step]
# - start: inclusive (included)
# - stop: exclusive (NOT included, stops one before)
# - step: stride (default is 1)

text = "GemRain-Consulting-2026"
print("Full String :", text)

# Slicing from index 0 up to 7 (exclusive):
print("Slice [0:7]   (First 7 chars)    :", text[0:7])       # GemRain

# Leaving start empty defaults to 0:
print("Slice [:7]    (Same as [0:7])    :", text[:7])        # GemRain

# Leaving stop empty slices to the very end:
print("Slice [8:]    (From index 8 on)  :", text[8:])        # Consulting-2026

# Extracting the last 4 characters using negative index:
print("Slice [-4:]   (Last 4 chars)     :", text[-4:])       # 2026

# Using step to skip characters:
alphabet = "ABCDEFGHIJ"
print("\nAlphabet       :", alphabet)
print("Every 2nd char :", alphabet[::2]) # ACEGI

# The Pythonic String Reversal trick:
print("Reversed string:", alphabet[::-1]) # JIHGFEDCBA


# ===========================================================================
# SECTION 3: STRINGS ARE IMMUTABLE
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 3: STRING IMMUTABILITY")
print("=" * 70)

# "Immutable" means once a string is created, its characters CANNOT be changed!
# For example, you CANNOT do: text[0] = "J"
# (That raises TypeError: 'str' object does not support item assignment)

original = "Jello World"
print("Original with typo :", original)

# To fix it, you create a NEW string by slicing and concatenating:
fixed = "H" + original[1:]
print("Corrected string   :", fixed)


# ===========================================================================
# SECTION 4: CASE ALTERATION METHODS
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 4: CASE ALTERATION METHODS")
print("=" * 70)

sentence = "wELcoME tO pYThon fASttRaCk!"
print("Original   :", sentence)
print(".upper()   :", sentence.upper())       # All UPPERCASE
print(".lower()   :", sentence.lower())       # All lowercase
print(".title()   :", sentence.title())       # Capitalize Every Word
print(".capitalize():", sentence.capitalize()) # Capitalize only the first letter


# ===========================================================================
# SECTION 5: TRIMMING WHITESPACE (.strip(), .lstrip(), .rstrip())
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 5: TRIMMING WHITESPACE")
print("=" * 70)

# Raw user input often contains accidental spaces or newlines:
messy_user = "   ahmad_developer \n\t "
print("Messy string with spaces : [" + messy_user + "]")

# .strip() removes whitespace from BOTH ends:
clean_user = messy_user.strip()
print("After .strip()           : [" + clean_user + "]")

# You can also strip specific characters:
serial_number = "***SKU-88219***"
clean_serial = serial_number.strip("*")
print("Stripping asterisks      :", clean_serial)


# ===========================================================================
# SECTION 6: SEARCHING & REPLACING (.replace(), .find(), .count())
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 6: SEARCHING AND REPLACING")
print("=" * 70)

announcement = "Python 2 is an old version. Python 2 is no longer updated."
print("Original :", announcement)

# .replace(old, new) creates a new string with replacements:
updated_announcement = announcement.replace("Python 2", "Python 3")
print("Replaced :", updated_announcement)

# .count(substring) counts occurrences:
print("Count of 'Python' :", updated_announcement.count("Python"))

# .find(substring) returns the index of the first occurrence:
print("Index of 'old'    :", updated_announcement.find("old"))

# Checking prefixes and suffixes:
filename = "quarterly_financial_report.csv"
print("\nFilename                     :", filename)
print(".startswith('quarterly')     :", filename.startswith("quarterly"))
print(".endswith('.csv')            :", filename.endswith(".csv"))
print(".endswith('.pdf')            :", filename.endswith(".pdf"))


# ===========================================================================
# SECTION 7: SPLITTING AND JOINING (.split() & .join())
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 7: SPLITTING AND JOINING STRINGS")
print("=" * 70)

# .split(delimiter) cuts a string into pieces:
raw_csv_row = "Sarah,Engineering,Lead Architect,12000"
fields = raw_csv_row.split(",")
print("Raw string       :", raw_csv_row)
print("After .split(',') :", fields)
print("First item       :", fields[0])
print("Role             :", fields[2])

# .join() stitches items together using a separator:
words = ["Learning", "Python", "Is", "Awesome"]
joined_sentence = " ".join(words)
print("\nJoined with space :", joined_sentence)

joined_hyphen = "-".join(words)
print("Joined with hyphen:", joined_hyphen)


# ===========================================================================
# SECTION 8: MODERN F-STRINGS (FORMATTED STRING LITERALS)
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 8: MODERN F-STRINGS (THE GOLD STANDARD)")
print("=" * 70)

# F-strings start with an f before the quote: f"..."
# Any variable or math expression inside {curly_braces} is evaluated!
first_name = "Kamal"
total_score = 94.6789
rank = 1

# Basic interpolation:
print(f"Congratulations {first_name}, your score is {total_score}!")

# Formatting numbers with 2 decimal places (:.2f):
print(f"Formatted score : {total_score:.2f}%")

# Adding commas to large numbers (:,):
annual_revenue = 4580920.50
print(f"Annual Revenue  : RM {annual_revenue:,.2f}")

# Alignment and column padding:
print(f"| {first_name:<10} | Rank: {rank:>3} | Score: {total_score:>6.2f} |")


# ===========================================================================
# SECTION 9: PROJECT - USER DATA NORMALIZER SCRIPT
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 9: PROJECT - USER PROFILE NORMALIZER")
print("=" * 70)

# Simulating raw dirty customer input from a web portal:
raw_name = "   dAnIeL kHoO   "
raw_email = "  Daniel.Khoo@CORPORATE.COM  \n"
raw_phone = "012-345-6789"
raw_credit_card = "4532-8891-2304-9812"

# Step 1: Clean and title-case the full name
clean_name = raw_name.strip().title()

# Step 2: Clean and lowercase the email
clean_email = raw_email.strip().lower()

# Step 3: Extract username and domain without loops
email_parts = clean_email.split("@")
user_handle = email_parts[0]
company_domain = email_parts[1]

# Step 4: Mask the credit card (show only last 4 digits)
# Slicing the last 4 characters: [-4:]
card_last_four = raw_credit_card[-4:]
masked_card = "****-****-****-" + card_last_four

# Step 5: Output normalized profile using f-strings
print("NORMALIZED CUSTOMER RECORD")
print("-" * 45)
print(f"Customer Name  : {clean_name}")
print(f"Primary Email  : {clean_email}")
print(f"User Handle    : {user_handle}")
print(f"Company Domain : {company_domain}")
print(f"Phone Number   : {raw_phone}")
print(f"Payment Card   : {masked_card}")
print("-" * 45)
print("Module 4 Teaching Code finished successfully!")
