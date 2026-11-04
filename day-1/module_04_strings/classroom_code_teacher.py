# working with strings

course_name = "Python"
print("Original course name is: ", course_name)
print("The numbers of characters in the course name is: ", len(course_name))

# Positive indexing
print("\n\n")
print("First character is: ", course_name[0]) # P
print("Second character is: ", course_name[1]) # y
print("Third character is: ", course_name[2]) # t

# Negative indexing
print("Last character is: ", course_name[-1]) # n
print("Second last character is: ", course_name[-2]) # o
print("Third last character is: ", course_name[-3]) # h

#Syntexing
# Slicing
print("\n\n")
text = "Python-Essentials-2026"
print("Original text is: ", text)
print("First 6 characters are which is Python: ", text[0:6]) # Python
print("First 6 characters are which is Python: ", text[:6]) # Python
print("Characters from index 7 to 17 are Essentials: ", text[7:17]) # Essentials
print("Characters from index 18 to 23 are 2026: ", text[18:23]) # 2026
print("Characters from index 18 to 23 are 2026: ", text[18:]) # 2026
print("The last 4 characters are 2026: ", text[-4:]) # 2026

# Skipping characters
print("\n\n")
alphabet = "ABCEFGHIJ"
print("Original alphabet is: ", alphabet)
print("Every second character is: ", alphabet[::2]) # ACEGI
print("Every second character starting from index 1 is: ", alphabet[1::2]) # BDFHJ

#Jumping in reverse order
print("Every second character is: ", alphabet[::-2]) # ACEGI
print("Every second character is: ", alphabet[::-1]) # JIHGFECBA

#Working with lower and upper case
print("\n\n")
sentence = "Working With lower and upper case"
print("Original sentence is: ", sentence)
print("Sentence in upper case is: ", sentence.upper())
print("Sentence in lower case is: ", sentence.lower())
print("Sentence in title case is: ", sentence.title())
print("Sentence in capitalized case is: ", sentence.capitalize())

# Trimming & Replacing
print("\n\n")
text_with_spaces = "   Hello, World!   "
print("Original text is: ", text_with_spaces)
print("Text after trimming spaces is: ", text_with_spaces.strip())
model_number = "#2026-AB###"
print("Original model number is: ", model_number)
print("Model number after trimming # is: ", model_number.strip("#"))

latest_phone = "The Iphone 17 is the latest model of Iphone"
print("Original text is: ", latest_phone)
updated_phone = latest_phone.replace("Iphone 17", "Iphone 18")
print("Updated text is: ", updated_phone)

# joing the words
words = ["Python", "Essentials", "2026"]
print("Original words are: ", words)
joined_words = " ".join(words)
print("Joined words are: ", joined_words)

#More with terminal print
print("\n\n")
name = "Arman"
age = 35
print("My name is ", name, " and I am ", age, " years old.")
print(f"My name is {name} and I am {age} years old.")

print("\n\n")
price = 612412.2418294
car_name = "BMW"
print(f"The price of {car_name} is {price:.2f} RM.")
