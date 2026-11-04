class_date = "4/11/2026"
class_name = "Python Programming"
beginning_time = 9
end_time = 17
duration = end_time - beginning_time
fees = 125.50
# Boolean values
present = True
absent = False

print("The", class_name, "is done in ", class_date, "and costs", fees, "begining at", beginning_time)
print("\nDaily duration is ", end_time - beginning_time, "hours")
print("\nDaily duration is ", duration, "hours")

print("\nStudent is present:", present)
print("Student is absent:", absent)


# Working with variables types

float_variable = 125.50
int_variable = 125
print("\nThe type of float_variable is:", type(float_variable))
print("The type of int_variable is:", type(int_variable))
print(int_variable)
print("\n")
print(int_variable + 125.50)
print("\n" + str(int_variable), 125.50)

str_number = "125"
print("\n" + str_number , int_variable)
new_int_number = int(str_number)
print("\n" , type(new_int_number))
print("\n" , int(str_number) + int_variable)

new_int_variable = 420
new_float_number = float(new_int_variable)
print(round(new_float_number, 2))

# Working with boolean values
print("\n\n")
print("=" *70)

# Boolean are either True or False
present = True
absent = False
print ("Student is present:", present, type(present))
print("Student is absent:", absent, type(absent))

# Printing Falsy values
print("\n\n")
print("Printing Falsy values")
print("False:", bool(False))
print("None:", bool(None))
print("Zero:", bool(0))
print("Zero with decimals:", bool(0.0))
print("Empty string:", bool(""))
print("Empty list:", bool([]))

print("Student is absent", bool(0))
print("Student is absent", bool(0.0))
print("Student is absent", bool(""))
print("Student is absent", bool([]))
print("Student is absent", bool(None))

# Printing Truthy values
print("\n\n")
print("Printing Truthy values") 
print("True:", bool(True))
print("Non-zero integer:", bool(42))
print("Non-zero float:", bool(3.14))
print("Negative integer:", bool(-1))
print("Non-empty string:", bool("Arman"))
print("Non-empty list:", bool([1, 2, 3]))

print("Student is present", bool(1))
print("Student is present", bool(3.14))
print("Student is present", bool(0.0000001))
print("Student is absent", bool(0.0000000))
print("Student is present", bool(-35))
print("Student is present", bool("Arman"))
print("Student is present", bool([1, 2, 3]))

# Assigning multiple variables in one line
print("\n\n")
print("=" *70)

a, b, c = "cat", "dog", "bear"
e, f, g = "sparrow", "parrot", "pigeon"
print(a, b, c, "can eat meat", sep=" \\ ") 
print(e, f, g, "can fly", sep="| ") 
print(a, b, c, "cannot fly", sep=", ")