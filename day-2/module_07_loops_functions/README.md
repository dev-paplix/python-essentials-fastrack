# Module 7: Loops and Functions

---

## 1. Introduction to Loops: 'While' and 'For'

### The `for` Loop and Iteration Helpers
In Python, `for` loops iterate over any **iterable** object (lists, strings, tuples, dictionaries, generators):

```python
# range(start, stop, step)
for i in range(1, 10, 2):
    print(i) # 1, 3, 5, 7, 9

# enumerate(iterable, start=0) -> Gives both index and item
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}: {fruit}")

# zip(*iterables) -> Pairs elements across multiple sequences
names = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 92]
for name, score in zip(names, scores):
    print(f"{name} -> {score}")
```

### The `while` Loop & Loop Control
A `while` loop executes repeatedly as long as its conditional remains `True`:
- **`break`**: Exits the innermost loop immediately.
- **`continue`**: Skips the remainder of the current iteration and advances to the next.
- **The `else` clause in loops**: Executes **only if the loop terminates normally** without hitting a `break` statement!

```python
# Searching using loop-else
target = 42
numbers = [10, 25, 33, 42, 59]

for num in numbers:
    if num == target:
        print("Found target!")
        break
else:
    print("Target NOT found in list.") # Only runs if break was NOT triggered
```

---

## 2. Deep Dive into Python Functions

### Defining Functions, Return Types, and Docstrings
```python
def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Computes the area of a rectangle.
    
    Parameters:
        width (float): Horizontal dimension.
        height (float): Vertical dimension.
        
    Returns:
        float: Computed area.
    """
    return width * height
```

### Pure Functions vs Side Effects
- **Pure Function**: Given the same inputs, always returns the same output, and does NOT mutate external state or variables.
- **Side Effects**: Modifying global variables, writing to files, printing to console, or mutating passed-in mutable arguments.

---

## 3. Variable Scope and Parameter Architecture

### The LEGB Scope Resolution Rule
When Python encounters a variable name, it searches for it in this strict order:
1. **L**ocal: Inside the current function.
2. **E**nclosing: Inside any enclosing functions (closures).
3. **G**lobal: At the top level of the module/script.
4. **B**uilt-in: Python's built-in namespace (`len`, `range`, `print`).

### Variadic Parameters: `*args` and `**kwargs`
- `*args` packs arbitrary positional arguments into a **tuple**.
- `**kwargs` packs arbitrary keyword arguments into a **dict**.

```python
def flexible_logger(level: str, *messages, **metadata):
    combined_msg = " ".join(str(m) for m in messages)
    print(f"[{level.upper()}] {combined_msg}")
    for k, v in metadata.items():
        print(f"   {k}: {v}")

flexible_logger("info", "User", 101, "logged in from IP", ip="10.0.0.1", browser="Chrome")
```

### Keyword-Only Arguments
Force callers to name arguments explicitly using a bare `*`:
```python
def create_user(username: str, *, is_admin: bool = False):
    pass

create_user("alice", is_admin=True) # Valid
create_user("alice", True)          # TypeError!
```

---

## 4. List, Dictionary, and Set Comprehensions

Comprehensions provide concise, expressive syntax for creating new collections:

### List Comprehensions
```python
# Syntax: [expression for item in iterable if condition]
evens_squared = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

### Dictionary Comprehensions
```python
# Syntax: {key_expr: val_expr for item in iterable}
names = ["alice", "bob", "charlie"]
name_lengths = {name.title(): len(name) for name in names}
# {'Alice': 5, 'Bob': 3, 'Charlie': 7}
```

### Set Comprehensions
```python
# Automatically eliminates duplicates
unique_vowels = {char for char in "abracadabra" if char in "aeiou"}
# {'a'}
```

