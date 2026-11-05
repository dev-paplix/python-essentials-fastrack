def header(title):
    print("\n" + "=" * 70)
    print(f"{title.upper()}")
    print("=" * 70 + "\n")

header("Day 2 materials")
header("this is the second header")

list_a = [10, 20, 30]
list_b = [10, 20, 30]
list_c = list_a

# Arman bought Latte for 7RM
# Lee bought latte for 7RM

print(list_a == list_b)  # True, because the values are the same
print(list_a is list_b)  # False, because they are different objects in memory
print(list_a is list_c)  # True, because list_c references the same object as list_a

# Sentimental compoarison
val = None
print(f"val is None:{val is None}")

# Short-Circuit mechanics

header("Short-Circuit")

def expensive_finder():
    print("Looking for expensive goods")
    return True

print("Test 1: False and expensive_finder()")
if False and expensive_finder():
    pass

print(" I was not expensive")

print("Test 2: True and expensive_finder()")
if True and expensive_finder():
    pass
print(" I was not expensive")


# Guard the code against dividing by zero
divisor = 0
result = (divisor !=0) and (100/ divisor> 5)
print(f"\n Safe zero dividing return: {result}")

"""
Real if and bool usage
loan application:
21 years or older, and the person has never been bankrupt and credit score to be at least 650 and make at least 35K
age >= 21, barkrupcy = False, credit_score >=650, annual_income>=35000

"""
def loan_application(application: dict):
    if application.get("age", 0) <21:
        return "Rejected: you have to be minimum 21 years old"
    if application.get("bankrupt", False):
        return "Rejected: You are bankrupt"
    if application.get("credit_score", 0) < 650:
        return "Rejected: very bad credit"
    if application.get("income", 0.0) < 35000.00:
        return "Rejected: you have very low income"
    return "Approved you can proceed with loan"

applicant_1 = {"age": 16, "income": 50000, "credit_score": 700, "bankrupt": False}
applicant_2 = {"age": 25, "income": 50000, "credit_score": 600, "bankrupt": False}
applicant_3 = {"age": 30, "income": 50000, "credit_score": 800, "bankrupt": True}
applicant_4 = {"age": 35, "income": 29000, "credit_score": 800, "bankrupt": False}
applicant_5 = {"age": 45, "income": 90000, "credit_score": 800, "bankrupt": False}

header("Loan Evaluation")
print(f"\nApplicant 1 loan application:{loan_application(applicant_1)}")
print(f"\nApplicant 2 loan application:{loan_application(applicant_2)}")
print(f"\nApplicant 3 loan application:{loan_application(applicant_3)}")
print(f"\nApplicant 4 loan application:{loan_application(applicant_4)}")
print(f"\nApplicant 5 loan application:{loan_application(applicant_5)}")

"""
Use if and elif, or, and

For those who get betwenn 90 to 100, they get A, for those who get 80-89 they get B, for those who get 70-79 get C and for those
who get less than 70 or absent they exam will be schedulled for next week
"""
header("Exam Marker")
grade = 70
status = "Present"

if grade >=90 and grade <=100 and status !="Absent":
    print("Congratulation you got A")
elif grade >=80 and grade <=89 and status !="Absent":
    print("Good job you got B")
elif grade >=71 and grade <=79 and status !="Absent":
    print("You passed with C")
elif grade ==70 and status !="Absent":
    print("You barely pass")
elif grade < 69 or status !="Present":
    print("You are scheduled for next week")
else:
    print("invalid input")
