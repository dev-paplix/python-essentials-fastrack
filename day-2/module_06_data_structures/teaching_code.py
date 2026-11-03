"""
Module 6: Data Structures in Python - Teaching Code
Instructor Demonstration Script
Course: Python Essentials FastTrack
"""

import copy

def header(title: str):
    print("\n" + "=" * 60)
    print(f" {title.upper()} ")
    print("=" * 60)

# =====================================================================
# 1. Lists: Dynamic Mutation, Slicing & Operations
# =====================================================================
header("1. List Operations & In-Place Mutations")

stack = []
print("Pushing elements onto stack:")
stack.append("Task 1")
stack.append("Task 2")
stack.append("Task 3")
print(f"Current Stack: {stack}")

popped = stack.pop()
print(f"Popped item: '{popped}', Stack remaining: {stack}")

# Inserting and removing
tasks = ["Setup", "Test", "Deploy"]
tasks.insert(1, "Code Review")
print(f"After insert: {tasks}")
tasks.remove("Setup")
print(f"After remove: {tasks}")

# =====================================================================
# 2. Dictionaries: Fast Hashing, Keys & Views
# =====================================================================
header("2. Dictionary Mapping & Safe Access")

server_config = {
    "host": "192.168.1.50",
    "port": 8080,
    "ssl_enabled": True,
    "allowed_origins": ["localhost", "gemrain.net"]
}

# Safe lookup with .get()
timeout = server_config.get("timeout_seconds", 30)
print(f"Server host : {server_config['host']}")
print(f"Timeout (with default) : {timeout}")

# Iterating keys, values, items
print("\nIterating key-value pairs:")
for key, val in server_config.items():
    print(f"  {key:<18}: {val}")

# Dictionary update (merging)
patch = {"port": 8443, "max_connections": 1000}
server_config.update(patch)
print(f"\nAfter config patch: port={server_config['port']}, max_conn={server_config['max_connections']}")

# =====================================================================
# 3. Shallow Copy vs Deep Copy Demonstration
# =====================================================================
header("3. Shallow Copy vs Deep Copy Memory Traps")

department_original = {
    "name": "Engineering",
    "teams": ["Frontend", "Backend"]
}

shallow_clone = department_original.copy()
deep_clone = copy.deepcopy(department_original)

# Mutate nested list inside shallow clone
shallow_clone["teams"].append("DevOps")

print(f"Original teams     : {department_original['teams']} (MUTATED by shallow copy!)")
print(f"Shallow copy teams : {shallow_clone['teams']}")
print(f"Deep copy teams    : {deep_clone['teams']} (Protected from mutation)")

# =====================================================================
# 4. Sorting Complex Collections with Lambdas
# =====================================================================
header("4. Sorting with Custom Keys (Lambdas)")

products = [
    {"sku": "A10", "name": "Mechanical Keyboard", "price": 120.0, "rating": 4.8},
    {"sku": "B22", "name": "Ergonomic Mouse", "price": 45.0, "rating": 4.9},
    {"sku": "C35", "name": "Ultrawide Monitor", "price": 450.0, "rating": 4.6},
    {"sku": "D41", "name": "USB-C Hub", "price": 30.0, "rating": 4.3},
]

# Sort by price ascending
by_price = sorted(products, key=lambda p: p["price"])
print("Sorted by Price (Ascending):")
for p in by_price:
    print(f"  ${p['price']:>6.2f} - {p['name']}")

# Sort by rating descending
by_rating = sorted(products, key=lambda p: p["rating"], reverse=True)
print("\nSorted by Rating (Descending):")
for p in by_rating:
    print(f"  Rating: {p['rating']} - {p['name']}")

if __name__ == "__main__":
    print("\n[SUCCESS] Module 6 Teaching Code executed successfully!")

