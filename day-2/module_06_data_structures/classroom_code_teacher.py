import copy

def header(title):
    print("\n" + "=" * 70)
    print(f"{title.upper()}")
    print("=" * 60)

header("Lists")
stack = []
stack.append("Item 1")
stack.append("Item 2")
stack.append("Item 3")

print(f"The stack includes: {stack}")

popped = stack.pop()
print(f"\nThe poppled item: {popped}, Remaining: {stack}")

items = ["Samsung Galaxy", "Iphone 18", "OnePlus 15"]
items.insert(1, "Huawei")
print(f"\nAfter insert: {items}")
items.remove("Samsung Galaxy")
print(f"\nAfter Removing: {items}")


header("Dictionaries")

house_details = {
    "unit_location": "55 Petaling St",
    "price": 525800,
    "dicounted": True,
    "payment_mode": ["cash", "finance"]
}

# Lookup with get
max_sales_time = house_details.get("listing_days", 90)
print(f"House location: {house_details['unit_location']}")
print(f"Maximum market duration: {max_sales_time}")

# Iteration keys and values, items
print("\n Iterating key:")
for key, val in house_details.items():
    print(f"{key:<18}: {val}")

# Updating and adding
patch  = {"price": 515000, "min_deposit": 25000}
house_details.update(patch)
print(f"\n After implement patch the new price is {house_details['price']}, min_dep={house_details['min_deposit']}")
print("\n Iterating key:")
for key, val in house_details.items():
    print(f"{key:<18}: {val}")


header("Using the copy library")

mall_dir = {
    "floor": 3,
    "shops": ["Starbucks", "Zues", "Gigi Coffee"]
}


cloned_mall_dir = mall_dir.copy()
deep_clone = copy.deepcopy(mall_dir)

cloned_mall_dir["shops"].append("Pizza Hut")

print(f"\nOriginal shops: {mall_dir['shops']} ")
print(f"\nCopied one: {cloned_mall_dir['shops']} ")
print(f"\nProtected list: {deep_clone['shops']}")

header("Sorting the list advanced with Lambda")

students = [
    {"student_id": "stu-1001", "name": "Micheal Doe", "Grade": 90, "Age": 16},
    {"student_id": "stu-1002", "name": "Jane Lin", "Grade": 58, "Age": 17},
    {"student_id": "stu-1003", "name": "Henry Jordan", "Grade": 60, "Age": 14},
    {"student_id": "stu-1004", "name": "Wayne Wong", "Grade": 96, "Age": 13},
]

# Sort them by Grade in ascending
by_grade = sorted(students, key=lambda g: g["Grade"])
print("Sorted students by grade in ascending:")
for g in by_grade:
    print(f"{g["Grade"]:>6} - {g['name']}")

# Sort them by Age in descending
by_age = sorted(students, key=lambda g: g["Age"], reverse=True)
print("\nSorted students by Age:")
for g in by_age:
    print(f"{g["Age"]:>6} - {g['student_id']} - {g['name']}")