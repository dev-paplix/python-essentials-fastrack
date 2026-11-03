# Module 2: Core Concepts — Variables and Data Types

---

## 1. Understanding Variables in Python

### Variables are "Name Tags", Not "Boxes"
In languages like C or Java, a variable is a named memory location with a fixed type:
```c
int score = 100; // Fixed 4-byte box holding 100
```
In Python, variables are **labels (pointers/references)** bound to objects in heap memory:
```python
score = 100
```
- The integer `100` is created as an object in heap memory.
- `score` is a reference tag pointing to that integer object.
- You can inspect the unique memory address of an object using `id(object)`.

### Dynamic Typing vs Static Typing
Python is **dynamically typed** and **strongly typed**:
- **Dynamically Typed**: Variable types are determined at runtime. A variable can point to an integer at one moment and a string the next:
  ```python
  data = 42          # data references an int
  data = "Python"    # now data references a str
  ```
- **Strongly Typed**: Python does not automatically coerce incompatible types without explicit conversion:
  ```python
  result = "Age: " + 25  # Raises TypeError: can only concatenate str to str
  result = "Age: " + str(25)  # Valid explicit casting!
  ```

### PEP 8 Naming Conventions
The official Python style guide (PEP 8) specifies:
- **Variables and functions**: `snake_case` (e.g., `user_account`, `total_score`).
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`, `TAX_RATE`).
- **Classes**: `PascalCase` (e.g., `StudentRecord`, `InvoiceProcessor`).
- **Reserved Keywords**: Never name variables `for`, `while`, `def`, `class`, `import`, `return`, `if`, etc.

---

## 2. Basic Data Types and Their Operations

Python includes five primary primitive types:

| Data Type | Class | Description | Example |
| :--- | :--- | :--- | :--- |
| **Integer** | `int` | Whole numbers of unlimited precision | `42`, `-17`, `1_000_000` |
| **Floating-Point** | `float` | Real numbers with decimal points (64-bit IEEE 754) | `3.14159`, `-0.001`, `1.5e3` |
| **String** | `str` | Immutable Unicode character sequence | `'hello'`, `"Python"`, `"""docs"""` |
| **Boolean** | `bool` | Subclass of `int` representing truth values | `True` (1), `False` (0) |
| **NoneType** | `NoneType`| Absence of a value or sentinel default | `None` |

### Type Inspection: `type()` vs `isinstance()`
- `type(obj)` returns the exact class of the object.
- `isinstance(obj, class_or_tuple)` returns `True` if `obj` is an instance of the class or any subclass (recommended for enterprise production code).
```python
x = 10
print(type(x))                  # <class 'int'>
print(isinstance(x, int))       # True
print(isinstance(x, (int, float))) # True (check multiple types)
```

### Explicit Type Casting
Convert between types using constructor functions:
- `int("123")` $\rightarrow$ `123`
- `float("3.14")` $\rightarrow$ `3.14`
- `str(456)` $\rightarrow$ `"456"`
- `bool(0)` $\rightarrow$ `False`, `bool(1)` $\rightarrow$ `True`, `bool("")` $\rightarrow$ `False`, `bool("hello")` $\rightarrow$ `True`

---

## 3. Variables and Script Updates

### Reassignment and Identity
```python
a = [1, 2, 3]
b = a          # b points to the same object as a
b.append(4)
print(a)       # [1, 2, 3, 4] -> Both changed because lists are mutable!

x = 10
y = x          # y points to 10
x += 5         # x now points to 15 (integers are immutable)
print(y)       # y remains 10
```

### Multiple and Augmented Assignments
```python
# Unpacking / Multiple Assignment
x, y, z = 10, 20, 30

# Elegant Python Swapping (no temp variable needed!)
x, y = y, x

# Augmented Assignment
count = 0
count += 1   # Equivalent to count = count + 1
count *= 2   # Equivalent to count = count * 2
count //= 2  # Floor divide in-place
```

---

## 4. Summary & Quiz
- Python variables are object references; use `id()` to inspect memory locations.
- Python is strongly and dynamically typed.
- Prefer `isinstance()` over `type()` when validating types.
- Numbers and strings are **immutable**; updating them re-binds the variable to a new object.

