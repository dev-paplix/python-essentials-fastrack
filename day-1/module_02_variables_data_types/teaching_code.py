"""
=============================================================================
Course   : Python Essentials [FastTrack] - Day 1
Module   : Module 2 - Core Concepts: Variables and Data Types
Audience : Absolute Beginners
Topic    : Instructor Teaching Code & Live Demonstration Script
=============================================================================

PEDAGOGICAL RULE FOR MODULE 2:
- Builds strictly upon Module 1.
- Explores variables, memory references, primitive types, type conversion.
- NO functions (def) - that is Module 7!
- NO conditionals (if / else) - that is Module 5!
- NO loops (for / while) - that is Module 7!
- Pure, sequential, step-by-step beginner code.
=============================================================================
"""

# ===========================================================================
# SECTION 1: VARIABLES AS LABELS & MEMORY REFERENCES (id)
# ===========================================================================
print("=" * 70)
print("SECTION 1: VARIABLES AS LABELS IN MEMORY")
print("=" * 70)

# In Python, variables do NOT store values directly inside "boxes".
# Instead, an object is created in memory, and the variable name is a
# label (or pointer) pointing to that object.
score = 100
bonus = 100

print("Variable 'score' holds :", score)
print("Variable 'bonus' holds :", bonus)

# Python's built-in id() function reveals the unique memory address:
print("Memory address of score (id) :", id(score))
print("Memory address of bonus (id) :", id(bonus))
print("Notice that both variables point to the EXACT same memory location!")

# If we change score:
score = 250
print("\nAfter updating score = 250:")
print("Variable 'score' now holds   :", score)
print("New memory address of score  :", id(score))
print("Variable 'bonus' still holds :", bonus)
print("Memory address of bonus      :", id(bonus))


# ===========================================================================
# SECTION 2: THE 5 FUNDAMENTAL DATA TYPES
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 2: THE 5 PRIMITIVE DATA TYPES IN PYTHON")
print("=" * 70)

# 1. Integer (int): Whole numbers (positive, negative, zero)
item_count = 15
temperature = -4
population = 34_000_000 # You can use underscores for readability!

# 2. Floating-Point (float): Numbers with decimal points
product_price = 199.95
gravity = 9.807
ratio = 0.0025

# 3. String (str): Sequences of characters wrapped in quotes
company_name = "GemRain Consulting Sdn Bhd"
headquarters = 'Petaling Jaya, Selangor'

# 4. Boolean (bool): Truth values (Only True or False, capitalized!)
is_active = True
has_discount = False

# 5. NoneType (None): Represents the intentional absence of a value
secondary_phone = None

print("Integer example   :", item_count)
print("Float example     :", product_price)
print("String example    :", company_name)
print("Boolean example   :", is_active)
print("NoneType example  :", secondary_phone)


# ===========================================================================
# SECTION 3: CHECKING DATA TYPES WITH type()
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 3: INSPECTING DATA TYPES WITH type()")
print("=" * 70)

# The built-in type() function tells you exactly what kind of data an object is.
print("Type of item_count     :", type(item_count))
print("Type of product_price  :", type(product_price))
print("Type of company_name   :", type(company_name))
print("Type of is_active      :", type(is_active))
print("Type of secondary_phone:", type(secondary_phone))


# ===========================================================================
# SECTION 4: DYNAMIC TYPING IN PYTHON
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 4: DYNAMIC TYPING")
print("=" * 70)

# In languages like C or Java, a variable can only ever hold ONE type.
# In Python, variables are dynamically typed: a variable can point to an
# integer at first, and later point to a string or float!

dynamic_var = 500
print("dynamic_var holds :", dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = "Now I am a piece of text!"
print("dynamic_var holds :", dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = 3.14159
print("dynamic_var holds :", dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = True
print("dynamic_var holds :", dynamic_var, "| Type:", type(dynamic_var))


# ===========================================================================
# SECTION 5: STRONG TYPING & THE NEED FOR TYPE CASTING
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 5: PYTHON IS STRONGLY TYPED")
print("=" * 70)

# Strongly typed means Python will NOT secretly convert types for you
# if they are incompatible.
# For example, you CANNOT do: "Total: " + 100
# That causes: TypeError: can only concatenate str to str, not "int".

# Solution: EXPLICIT TYPE CASTING!
# Convert the number 100 into text using str():
total_amount = 100
message = "Total: RM " + str(total_amount)
print("Properly concatenated string:", message)


# ===========================================================================
# SECTION 6: TYPE CASTING FUNCTIONS (int, float, str, bool)
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 6: CONVERTING BETWEEN DATA TYPES")
print("=" * 70)

# 1. Converting String to Integer: int()
str_number = "450"
converted_int = int(str_number)
print("String '450' to int :", converted_int, "| Type:", type(converted_int))
print("Math check (450 + 50):", converted_int + 50)

# 2. Converting String to Float: float()
str_price = "89.95"
converted_float = float(str_price)
print("String '89.95' to float :", converted_float, "| Type:", type(converted_float))
print("Math check (89.95 * 2)  :", converted_float * 2)

# 3. Converting Float to Integer (TRUNCATES decimals, does NOT round!):
original_float = 9.99
truncated_int = int(original_float)
print("int(9.99) truncates to :", truncated_int)

# 4. Converting Integer to Float:
original_int = 42
converted_float = float(original_int)
print("float(42) becomes      :", converted_float)


# ===========================================================================
# SECTION 7: TRUTHINESS AND THE bool() CONVERSION
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 7: TRUTHY AND FALSY VALUES WITH bool()")
print("=" * 70)

# In Python, every single object can be evaluated as either True or False!
# The rule is simple:
# "EMPTY" or "ZERO" values are FALSY (False).
# "NON-EMPTY" or "NON-ZERO" values are TRUTHY (True).

print("FALSY VALUES:")
print("bool(0)     :", bool(0))        # Zero integer
print("bool(0.0)   :", bool(0.0))      # Zero float
print("bool('')    :", bool(""))       # Empty string
print("bool(None)  :", bool(None))     # None object

print("\nTRUTHY VALUES:")
print("bool(1)        :", bool(1))         # Non-zero integer
print("bool(-10)      :", bool(-10))       # Negative integer is also non-zero!
print("bool('hello')  :", bool("hello"))   # Non-empty string
print("bool(' ')      :", bool(" "))       # A single space is non-empty!


# ===========================================================================
# SECTION 8: MULTIPLE ASSIGNMENT AND VALUE SWAPPING
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 8: MULTIPLE ASSIGNMENT & PYTHONIC SWAPPING")
print("=" * 70)

# Assign multiple variables on a single line:
x, y, z = 10, 20, 30
print("x =", x, "| y =", y, "| z =", z)

# Assigning the SAME value to multiple variables:
status_a = status_b = status_c = "PENDING"
print("status_a:", status_a, "| status_b:", status_b, "| status_c:", status_c)

# SWAPPING VALUES:
# In C/Java, you need a temporary third variable (temp = a; a = b; b = temp;).
# In Python, swapping is done in ONE elegant line:
player1 = "Alice"
player2 = "Bob"
print("\nBefore swapping : Player 1 =", player1, "| Player 2 =", player2)

# Pythonic Swap:
player1, player2 = player2, player1
print("After swapping  : Player 1 =", player1, "| Player 2 =", player2)


# ===========================================================================
# SECTION 9: AUGMENTED ASSIGNMENT OPERATORS (+=, -=, *=, /=)
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 9: AUGMENTED ASSIGNMENT OPERATORS")
print("=" * 70)

counter = 100
print("Initial counter :", counter)

counter += 25  # Equivalent to: counter = counter + 25
print("counter += 25   :", counter)

counter -= 15  # Equivalent to: counter = counter - 15
print("counter -= 15   :", counter)

counter *= 2   # Equivalent to: counter = counter * 2
print("counter *= 2    :", counter)

counter /= 4   # Equivalent to: counter = counter / 4 (always returns float)
print("counter /= 4    :", counter)


# ===========================================================================
# SECTION 10: REAL-WORLD PROJECT - E-COMMERCE RECEIPT BUILDER
# ===========================================================================
print("\n" + "=" * 70)
print("SECTION 10: PROJECT - E-COMMERCE RECEIPT WITH PROPER TYPE CASTING")
print("=" * 70)

# Imagine receiving string inputs from an online order form:
input_item = "Ergonomic Mechanical Keyboard"
input_unit_price = "249.90"
input_qty = "3"
input_discount_rate = "0.10"
input_shipping = "15.00"

# Step 1: Explicitly convert inputs to proper numbers
unit_price = float(input_unit_price)
quantity = int(input_qty)
discount_rate = float(input_discount_rate)
shipping_fee = float(input_shipping)

# Step 2: Compute order financials
subtotal = unit_price * quantity
discount_amount = subtotal * discount_rate
tax_amount = (subtotal - discount_amount) * 0.06
grand_total = subtotal - discount_amount + tax_amount + shipping_fee

# Step 3: Output formatted receipt
print("RECEIPT - GEMRAIN TECH STORE")
print("----------------------------------------")
print("Item Purchased :", input_item)
print("Quantity       :", quantity, "@ RM", unit_price)
print("Subtotal       : RM", subtotal)
print("Discount (10%) : -RM", discount_amount)
print("Sales Tax (6%) : RM", tax_amount)
print("Shipping Fee   : RM", shipping_fee)
print("----------------------------------------")
print("TOTAL PAYABLE  : RM", grand_total)
print("----------------------------------------")
print("Script executed successfully without functions or loops!")
