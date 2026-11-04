# Section 1: the first line of code
print("=" * 70)
print("This is Section 1: the first line of code")
print("=" * 70)


# Single quote and double quote strings
print('This is a single quote string')
print("This is a double quote string")
print("="*70)
print("'This is a single quote' inside a double quote string")
print("="*70)
print("\n\nThis is a double quote string")
print("="*70)
print("\n" + "This is another string " + "This is my second string")
print("="*70)
print("\n" + "This is another string", "This is my second string")

# Working with numbers
print("="*70)
print("\n\n")
print("Day", 1)
print("The amount is:", 125.50)
print("20 "+"30")
print(20 + 30)
print(20.3 + 30.5)

# Working with seperators
print("="*70)
print("\n\n")

print("cat", "dog", "mouse", sep=", ")
print("cat", "dog", "mouse", sep="| ")
print("cat", "dog", "mouse", sep="- ")
print("cat", "dog", "mouse", sep="@ ")
print("cat", "dog", "mouse", sep=" \\ ")

print("Loading the file", end=" ...")

# Working with arithmetic operators
print("="*70)
print("\n\n")

print("Addition:", 20 + 30)
print("Subtraction:", 30 - 20)
print("Multiplication:", 20 * 30)
print("Division:", 30 / 20)
print("Division:", 100 / 30)
print("Division:", round(100 / 30, 6)) # With certain numbers of decimal places
print("Exponentiation:", 2 ** 3)
print("Modulus:", 10 % 3)
print("Floor Division:", 10 // 3)
