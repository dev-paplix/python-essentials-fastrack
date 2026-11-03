"""
=============================================================================
Course   : Python Essentials [FastTrack] - Day 1
Module   : Module 1 - Introduction to Python
Audience : Absolute Beginners (No prior programming experience required)
Topic    : Instructor Teaching Code & Live Demonstration Script
=============================================================================

PEDAGOGICAL RULE FOR MODULE 1:
- NO functions (def)
- NO conditionals (if / elif / else)
- NO loops (for / while)
- NO complex collections (lists / dicts)
- Pure, sequential, top-to-bottom beginner Python!
=============================================================================
"""

# ===========================================================================
# SECTION 1: THE VERY FIRST PYTHON COMMAND - print()
# ===========================================================================
print("=" * 70)
print("SECTION 1: YOUR VERY FIRST PYTHON COMMAND")
print("=" * 70)

# The print() function displays whatever is placed inside its parentheses
# to the console/terminal screen.
print("Hello, World!")
print("Welcome to Python Essentials FastTrack!")
print("Python is fun, readable, and powerful.")


# ===========================================================================
# SECTION 2: TEXT LITERALS - SINGLE VS DOUBLE QUOTES
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 2: STRINGS AND QUOTATION MARKS")
print("=" * 70)

# In Python, text is called a "string" (short for string of characters).
# You can use either double quotes ("...") or single quotes ('...').
print("This string is enclosed in double quotes.")
print('This string is enclosed in single quotes.')

# Why does Python allow both? So you can easily include quotes inside text!
print("He said, 'Python is amazing!' to the class.")
print('It is a great day to learn Python, isn\'t it?')
print('She replied: "Let\'s start coding right now!"')


# ===========================================================================
# SECTION 3: PRINTING MULTIPLE ITEMS IN A SINGLE LINE
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 3: PRINTING MULTIPLE ITEMS SEPARATED BY COMMAS")
print("=" * 70)

# You can pass multiple items into print() separated by commas.
# By default, Python automatically places a single space between them.
print("Python", "Essentials", "Training", "2026")
print("Day", 1, "Module", 1)
print("The answer is:", 42)


# ===========================================================================
# SECTION 4: CUSTOMIZING SEPARATORS WITH sep=
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 4: CUSTOMIZING THE SEPARATOR (sep=)")
print("=" * 70)

# The 'sep' parameter allows you to choose what appears between items.
# Default is a space: sep=" "
print("apple", "banana", "cherry")                     # Default space
print("apple", "banana", "cherry", sep=", ")           # Comma and space
print("apple", "banana", "cherry", sep=" | ")          # Vertical pipes
print("2026", "11", "03", sep="-")                     # Date format
print("user", "gemrain", "net", sep="@")               # Custom character
print("C:", "Users", "papli", "Documents", sep="\\")   # File path look


# ===========================================================================
# SECTION 5: CONTROLLING LINE ENDINGS WITH end=
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 5: CONTROLLING LINE ENDINGS (end=)")
print("=" * 70)

# By default, print() automatically moves to a new line after executing.
# That is because the default line ending is end="\n" (newline).
# You can change 'end' to anything you want!
print("First sentence.")
print("Second sentence.")

print("\nPrinting on the same line using end=' ':")
print("Loading", end="...")
print("Please wait", end="...")
print("Complete!", end="\n")

print("\nPrinting a progress indicator:")
print("[", end="")
print("■■■■■■■■■■", end="")
print("] 100% DONE")


# ===========================================================================
# SECTION 6: SPECIAL CHARACTERS (ESCAPE SEQUENCES)
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 6: ESCAPE SEQUENCES (\\n, \\t, \\\\)")
print("=" * 70)

# The backslash (\) is a special escape character in Python.
# \n -> creates a brand new line
# \t -> inserts a tab (indentation)
# \\ -> prints a literal backslash
# \" -> prints a literal double quote

print("Line 1\nLine 2\nLine 3")
print("Student\t\tGrade\tStatus")
print("Ali\t\t95\tPass")
print("Siti\t\t88\tPass")
print("John\t\t92\tPass")
print("File location: C:\\Program Files\\Python311\\python.exe")


# ===========================================================================
# SECTION 7: COMMENTS AND DOCUMENTING YOUR CODE
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 7: CODE COMMENTS (HOW COMPUTERS IGNORE TEXT)")
print("=" * 70)

# Any line starting with a hash symbol (#) is a comment.
# Python completely ignores comments during execution.
# Comments are written for human readers: you, your team, and your future self.

# This line does nothing at all!
print("Only this line actually runs.") # You can also add comments at the end of a line!

# Multi-line text / docstrings:
print("""
This is a multi-line string.
It preserves all the line breaks
and spaces exactly as you type them.
Very handy for long text blocks and ASCII art!
""")


# ===========================================================================
# SECTION 8: PYTHON AS A DIRECT CALCULATOR
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 8: USING PYTHON AS A CALCULATOR")
print("=" * 70)

# Notice: Numbers do NOT use quotation marks!
# If you put quotes around numbers, Python treats them as plain text!
print("Addition        (10 + 5) :", 10 + 5)
print("Subtraction     (20 - 7) :", 20 - 7)
print("Multiplication  (6 * 8)  :", 6 * 8)
print("Division        (15 / 3) :", 15 / 3)
print("Parentheses     ((2+3)*4):", (2 + 3) * 4)

# Text vs Number Demonstration:
print("\nLook at the difference quotation marks make:")
print("5 + 5 as text    :", "5 + 5")
print("5 + 5 as numbers :", 5 + 5)


# ===========================================================================
# SECTION 9: INTRODUCING VARIABLES - STORING INFORMATION
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 9: WHAT IS A VARIABLE?")
print("=" * 70)

# Think of a variable as a labeled sticky note attached to a piece of data.
# Syntax: variable_name = value
# The single '=' sign means ASSIGN (store the value on the right into the name on the left).

student_name = "Farah Aziz"
course_name = "Python Essentials [FastTrack]"
training_days = 3
course_fee = 1200.00
is_completed = False

# We can now use these variables anytime!
print("Participant Name :", student_name)
print("Enrolled Course  :", course_name)
print("Course Duration  :", training_days, "days")
print("Total Tuition    : RM", course_fee)


# ===========================================================================
# SECTION 10: SEQUENTIAL EXECUTION - TOP TO BOTTOM
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 10: SEQUENTIAL EXECUTION (LINE-BY-LINE FLOW)")
print("=" * 70)

# Python reads code like a book: line 1, then line 2, then line 3.
# Code never jumps backwards unless instructed by loops or functions.
step_1 = "Wake up in the morning"
step_2 = "Eat a hearty breakfast"
step_3 = "Open laptop and launch Python IDE"
step_4 = "Write and execute first Python code"

print("Step 1:", step_1)
print("Step 2:", step_2)
print("Step 3:", step_3)
print("Step 4:", step_4)


# ===========================================================================
# SECTION 11: UPDATING AND REASSIGNING VARIABLES
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 11: REASSIGNING VARIABLES")
print("=" * 70)

# Variables can change (vary) over time.
current_score = 0
print("Initial score    :", current_score)

# We update the score:
current_score = 50
print("After Exercise 1 :", current_score)

# We update it again:
current_score = 100
print("After Exercise 2 :", current_score)


# ===========================================================================
# SECTION 12: THE INPUT-PROCESS-OUTPUT (IPO) MODEL IN ACTION
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 12: THE INPUT - PROCESS - OUTPUT (IPO) WORKFLOW")
print("=" * 70)

# All computer software follows IPO:
# 1. INPUT   : Gather information
# 2. PROCESS : Calculate, format, or transform that information
# 3. OUTPUT  : Display or store the result

# Simulated inputs (in interactive mode, you would use input()):
user_first_name = "Kumar"
user_last_name = "Suresh"
organization = "Petronas Digital"
daily_training_hours = 8
number_of_days = 3

# PROCESS:
full_name = user_first_name + " " + user_last_name
total_hours_invested = daily_training_hours * number_of_days

# OUTPUT:
print("Full Name           :", full_name)
print("Company / Org       :", organization)
print("Total Program Hours :", total_hours_invested, "hours")


# ===========================================================================
# SECTION 13: MINI-PROJECT - CONFERENCE ATTENDEE BADGE GENERATOR
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 13: MINI-PROJECT - CONFERENCE ATTENDEE BADGE")
print("=" * 70)

badge_attendee = "DR. AISHA AL-MANSOOR"
badge_role = "AI RESEARCH SCIENTIST"
badge_company = "TECHVENTURES MALAYSIA"
badge_track = "PYTHON ESSENTIALS 2026"

print("+" + "-" * 42 + "+")
print("|" + " " * 11 + "CONFERENCE PASS 2026" + " " * 11 + "|")
print("+" + "-" * 42 + "+")
print("| ATTENDEE : " + badge_attendee + " " * (30 - len(badge_attendee)) + "|")
print("| ROLE     : " + badge_role + " " * (30 - len(badge_role)) + "|")
print("| COMPANY  : " + badge_company + " " * (30 - len(badge_company)) + "|")
print("| TRACK    : " + badge_track + " " * (30 - len(badge_track)) + "|")
print("+" + "-" * 42 + "+")
print("| [||||||||||||||||||||||||||||||||||||]   |")
print("|           SCAN AT MAIN GATES             |")
print("+" + "-" * 42 + "+")


# ===========================================================================
# SECTION 14: COMMON BEGINNER ERRORS & HOW TO FIX THEM
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 14: COMMON BEGINNER SYNTAX MISTAKES (SHOWN IN COMMENTS)")
print("=" * 70)

# MISTAKE 1: Case Sensitivity
# Print("Hello")   -> NameError: name 'Print' is not defined. Python is case-sensitive! Use 'print'.

# MISTAKE 2: Missing Quotes around text
# print(Hello)     -> NameError: name 'Hello' is not defined. Python thinks Hello is a variable!

# MISTAKE 3: Unmatched Quotes
# print("Hello')   -> SyntaxError: unterminated string literal. Opening and closing quotes must match!

# MISTAKE 4: Missing Parentheses
# print "Hello"    -> SyntaxError: Missing parentheses in call to 'print'. (This was Python 2 syntax!)

# MISTAKE 5: Misspelled variable names
# my_score = 100
# print(my_scrore) -> NameError: name 'my_scrore' is not defined. Check spelling carefully!

print("Instructor demonstration complete! You are now ready for the exercises.")
print("=" * 70)
