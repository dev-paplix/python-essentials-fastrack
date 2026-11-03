# Module 6: Data Structures in Python

---

## 1. Lists: Sequences and Operations

### What is a List?
A `list` is a **mutable, ordered sequence** of heterogenous Python objects. Lists are dynamic arrays internally, allowing $O(1)$ amortized append and index lookups.

### Common List Methods
```python
fruits = ["apple", "banana"]

# Appending & Extending
fruits.append("cherry")         # ['apple', 'banana', 'cherry']
fruits.extend(["date", "fig"])  # ['apple', 'banana', 'cherry', 'date', 'fig']
fruits.insert(1, "blueberry")   # Inserts at index 1

# Removal
popped_item = fruits.pop()      # Removes and returns last element ('fig')
popped_idx = fruits.pop(0)      # Removes element at index 0 ('apple')
fruits.remove("banana")         # Removes first occurrence of "banana"

# Reordering
fruits.sort()                   # In-place alphabetical sort
fruits.reverse()                # In-place reversal
```

---

## 2. Dictionaries: Hash Maps and Fast Lookups

### What is a Dictionary?
A `dict` is an **unordered (ordered by insertion since Python 3.7+), mutable mapping** of unique keys to arbitrary values. Dictionaries use hash tables under the hood, delivering average $O(1)$ constant time complexity for insertions, updates, and lookups.

### Keys Must Be Hashable
Dictionary keys must be immutable objects whose hash does not change during their lifetime:
- **Valid Keys**: `int`, `float`, `str`, `tuple`, `frozenset`.
- **Invalid Keys**: `list`, `dict`, `set` (raises `TypeError: unhashable type`).

### Key Dictionary Methods
```python
user = {"id": 101, "name": "Sarah", "role": "Engineer"}

# Safe retrieval (avoids KeyError)
role = user.get("role", "DefaultRole")        # Returns "Engineer"
salary = user.get("salary", 0.0)             # Returns 0.0 without throwing KeyError

# Traversing key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")

# Updates & Merging (Python 3.9+ supports the pipe operator '|')
user.update({"role": "Lead Architect", "active": True})
# Or: updated_user = user | {"location": "Kuala Lumpur"}
```

---

## 3. Advanced Methods for List Manipulation

### Shallow Copy vs Deep Copy
When a list contains nested mutable structures (e.g., lists of lists or lists of dicts), standard `.copy()` or slicing `[:]` performs only a **shallow copy**:
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow = original.copy()
deep = copy.deepcopy(original)

shallow[0][0] = 999
print(original[0][0])  # 999! The nested list was mutated in both!

deep[0][0] = 111
print(original[0][0])  # Still 999! Deep copy completely duplicated memory trees.
```

### Sorting with Custom Keys (`key=lambda`)
The `.sort()` method and `sorted()` function accept a `key` parameter:
```python
employees = [
    {"name": "Alice", "salary": 85000, "dept": "HR"},
    {"name": "Bob", "salary": 110000, "dept": "IT"},
    {"name": "Charlie", "salary": 95000, "dept": "Finance"},
]

# Sort by salary ascending:
employees.sort(key=lambda emp: emp["salary"])

# Sort by name length descending:
sorted_by_len = sorted(employees, key=lambda emp: len(emp["name"]), reverse=True)
```

---

## 4. Practical Project: Inventory Management System
We build a full relational-style in-memory inventory management engine capable of:
- Adding and restocking items.
- Depleting stock during orders with quantity validation.
- Generating low-stock alerts.
- Calculating total valuation.

