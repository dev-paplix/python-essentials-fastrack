# Module 7: Loops, Arrays, and Functions

---

## Overview & Learning Objectives

This module equips you with essential patterns for iteration, data structure traversal, and procedural modularity in Python:
- **Foundations of Loops**: Mastering `for` and `while` loops, `range()` stepping, `enumerate()`, `zip()`, and loop control (`break`, `continue`, `pass`, `else`).
- **Ternary Conditional Expressions**: Utilizing `<true_val> if <condition> else <false_val>` for concise inline decision-making and data mapping.
- **Multi-Dimensional Array Traversal**: Traversing and manipulating **1D arrays**, **2D matrices/grids**, and **3D volumes/tensors** using single and nested loops.
- **Function Architecture & Best Practices**: Defining reusable functions, type hints, docstrings, pure functions vs side effects.
- **Variable Scope (LEGB Rule)**: Understanding Local, Enclosing, Global, and Built-in scopes, along with `global` and `nonlocal` keywords.
- **Advanced Parameter Handling**: Packing and unpacking with `*args`, `**kwargs`, and enforcing keyword-only arguments.
- **Modern Comprehensions**: Constructing expressive list, dictionary, set, and nested multi-dimensional comprehensions.

---

## 1. Core Loop Fundamentals: `for` and `while` Loops

### 1.1 The `for` Loop and `range()`

In Python, the `for` loop iterates over items of any **iterable** sequence (lists, strings, tuples, dictionaries, sets, or range generators).

```python
# range(stop) -> 0 to stop-1
for i in range(5):
    print(i, end=" ") # 0 1 2 3 4

# range(start, stop) -> start to stop-1
for i in range(10, 15):
    print(i, end=" ") # 10 11 12 13 14

# range(start, stop, step) -> stepping by step
for i in range(0, 20, 5):
    print(i, end=" ") # 0 5 10 15

# Negative step (Countdown)
for i in range(5, 0, -1):
    print(i, end=" ") # 5 4 3 2 1
```

#### Iterating Sequences
```python
# Iterating over string characters
for char in "PYTHON":
    print(char, end="-") # P-Y-T-H-O-N-

# Iterating over dictionary keys, values, or key-value pairs
user = {"id": 101, "role": "admin", "active": True}
for key, val in user.items():
    print(f"{key} => {val}")
```

---

### 1.2 Iteration Helpers: `enumerate()` and `zip()`

#### `enumerate(iterable, start=0)`
Supplies both the index counter and the element in each iteration:
```python
fruits = ["Apple", "Banana", "Cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 1: Apple
# 2: Banana
# 3: Cherry
```

#### `zip(*iterables)`
Iterates in parallel across multiple sequences, pairing corresponding elements into tuples:
```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 92]
grades = ["A", "B+", "A"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name:<8} Score={score} Grade={grade}")
```

---

### 1.3 The `while` Loop

A `while` loop runs repeatedly as long as its condition evaluates to `True`.

#### Counter-Driven Loop
```python
counter = 3
while counter > 0:
    print(f"Counting down: {counter}")
    counter -= 1
```

#### Condition-Driven Retry Loop
```python
attempt = 1
max_retries = 3
success = False

while attempt <= max_retries and not success:
    print(f"Connecting to service (attempt {attempt})...")
    # Simulate success on attempt 2
    if attempt == 2:
        success = True
        print("Connected!")
    attempt += 1
```

---

### 1.4 Loop Control Statements: `break`, `continue`, `pass`

| Statement | Behavior |
| :--- | :--- |
| `break` | Immediately terminates the loop and moves execution to the statement after the loop. |
| `continue` | Aborts the remainder of the current iteration and jumps directly to the next cycle. |
| `pass` | Syntactic placeholder (no-op) used when a code block is syntactically required but no action is needed. |

```python
# Using continue to skip even numbers
for n in range(1, 10):
    if n % 2 == 0:
        continue
    print(n, end=" ") # 1 3 5 7 9
```

---

### 1.5 The Loop `else` Clause (Sentinel Search Pattern)

In Python, both `for` and `while` loops can have an optional `else` block.
- The `else` block executes **only if the loop completes normally** (i.e., without encountering a `break` statement).
- If the loop exits early via `break`, the `else` block is **skipped**.

```python
# Sentinel search for a target value
numbers = [10, 25, 33, 42, 59]
target = 99

for num in numbers:
    if num == target:
        print(f"Found target: {num}")
        break
else:
    print("Target NOT found in the list.") # Executes because loop finished without break
```

---

## 2. The Ternary Conditional Operator

The ternary conditional operator in Python allows conditional evaluation in a single line:

$$\text{value\_if\_true} \quad \text{if} \quad \text{condition} \quad \text{else} \quad \text{value\_if\_false}$$

Unlike `if-else` blocks (which are **statements**), the ternary operator is an **expression** that evaluates to a value and can be assigned, returned, or embedded inside other expressions.

### 2.1 Basic Usage
```python
score = 75
result = "PASS" if score >= 60 else "FAIL"
print(result) # PASS

# Standalone assignment
status_code = 200
message = "OK" if status_code == 200 else "ERROR"
```

### 2.2 Ternary Operator Inside Loops
```python
readings = [18.2, 26.5, 31.0, 15.4, 29.8]

# Categorizing each reading inline
for temp in readings:
    status = "HOT" if temp >= 28.0 else "NORMAL"
    print(f"{temp} C -> {status}")

# Clamping values between 0.0 and 100.0
raw_values = [-5, 42, 120, 85, -12]
clamped_values = []
for v in raw_values:
    # Nested ternary: if v < 0 -> 0, elif v > 100 -> 100, else v
    bounded = 0 if v < 0 else (100 if v > 100 else v)
    clamped_values.append(bounded)
# [0, 42, 100, 85, 0]
```

### 2.3 Ternary Transformation vs Filtering in List Comprehensions

A common point of confusion is where `if` appears in a list comprehension:
1. **Value Transformation (Requires `if` and `else`)** placed **before** the `for`:
   ```python
   # Replaces negative numbers with 0, retains positives
   rectified = [x if x > 0 else 0 for x in [-2, 5, -1, 8]]
   # Output: [0, 5, 0, 8]
   ```
2. **Filtering (No `else`)** placed **after** the `for`:
   ```python
   # Filters out negative numbers entirely
   positives_only = [x for x in [-2, 5, -1, 8] if x > 0]
   # Output: [5, 8]
   ```

---

## 3. Looping with Arrays (1D, 2D, and 3D Arrays)

In Python, contiguous numerical and collection grids are represented using Python lists as dynamic arrays.

```
1D Array:       [ 10, 20, 30, 40 ]             Shape: (4,)
2D Matrix:      [ [1, 2, 3],                   Shape: (3, 3)
                  [4, 5, 6],
                  [7, 8, 9] ]
3D Tensor/Cube: [ [ [1, 2], [3, 4] ],          Shape: (2, 2, 2)
                  [ [5, 6], [7, 8] ] ]
```

---

### 3.1 1D Arrays (Lists)

#### Direct Element Traversal vs Index-Based Traversal
```python
scores = [88, 92, 79, 95, 64]

# Direct Traversal (Preferred for read-only scanning)
total = 0
for score in scores:
    total += score

# Index-Based Traversal (Required when modifying in-place or tracking neighbor elements)
for i in range(len(scores)):
    if scores[i] < 70:
        scores[i] += 5 # Curve lowest grades
```

#### Accumulator Patterns
```python
data = [14, 28, 9, 45, 33, 19]

total_sum = 0
min_val = data[0]
max_val = data[0]

for val in data:
    total_sum += val
    if val < min_val:
        min_val = val
    if val > max_val:
        max_val = val

average = total_sum / len(data)
```

---

### 3.2 2D Arrays (Grids / Matrices)

A 2D array is modeled as a **list of lists**, accessed via `matrix[row_index][column_index]`.

#### Structure & Coordinate Access
```python
# 3 Rows x 4 Columns Matrix
grid = [
    [10, 20, 30, 40], # Row 0
    [50, 60, 70, 80], # Row 1
    [90, 95, 98, 99]  # Row 2
]

# Access element at Row 1, Column 2 -> 70
val = grid[1][2]
```

#### Traversing with Nested `for` Loops
```python
num_rows = len(grid)
num_cols = len(grid[0])

# Row-major coordinate traversal
for r in range(num_rows):
    for c in range(num_cols):
        print(f"cell({r}, {c}) = {grid[r][c]}")
```

#### Row Sums and Column Sums
```python
# Calculating Row Totals
row_totals = []
for row in grid:
    row_totals.append(sum(row))
# [100, 260, 382]

# Calculating Column Totals across all rows
col_totals = []
for c in range(num_cols):
    col_sum = 0
    for r in range(num_rows):
        col_sum += grid[r][c]
    col_totals.append(col_sum)
# [150, 175, 198, 219]
```

#### Primary Diagonal of a Square Matrix
For an $N \times N$ matrix, diagonal elements share identical indices `matrix[i][i]`:
```python
square = [
    [5, 1, 9],
    [3, 7, 2],
    [8, 4, 6]
]

diagonal = [square[i][i] for i in range(len(square))]
# [5, 7, 6]
```

#### Applying Ternary Transformations Across a 2D Grid
```python
# Create a binary threshold mask: 1 if val >= 50 else 0
threshold_grid = []
for row in grid:
    masked_row = [1 if val >= 50 else 0 for val in row]
    threshold_grid.append(masked_row)
```

---

### 3.3 3D Arrays (Cubes / Tensors / Multi-layered Grids)

A 3D array is represented as a list of 2D matrices, indexed as `cube[depth][row][col]` (or `[layer][row][col]`).

#### Real-World Analogy: Multi-Story Office Building Sensors
Imagine a building with:
- 2 Floors (Depth / Layer)
- 3 Rooms per floor (Rows)
- 2 Environmental Sensors per room (Columns)

```python
building_temps = [
    # Floor 0
    [
        [20.5, 21.0],  # Room 0 (Sensors A, B)
        [22.0, 22.5],  # Room 1
        [19.8, 20.2]   # Room 2
    ],
    # Floor 1
    [
        [24.0, 24.5],  # Room 0
        [28.5, 29.0],  # Room 1 (Hotspot room!)
        [23.0, 23.5]   # Room 2
    ]
]
```

#### Traversing with 3 Nested Loops
```python
hotspot_threshold = 26.0
hotspots = []
total_sum = 0.0
count = 0

for floor_idx, floor in enumerate(building_temps):
    for room_idx, room in enumerate(floor):
        for sensor_idx, temp in enumerate(room):
            total_sum += temp
            count += 1
            if temp > hotspot_threshold:
                hotspots.append((floor_idx, room_idx, sensor_idx, temp))

overall_average = total_sum / count
# Hotspots: [(1, 1, 0, 28.5), (1, 1, 1, 29.0)]
```

#### Computing Layer Slice Averages (Floor Averages)
```python
floor_averages = []
for floor in building_temps:
    floor_sum = 0.0
    floor_readings = 0
    for room in floor:
        for temp in room:
            floor_sum += temp
            floor_readings += 1
    floor_averages.append(round(floor_sum / floor_readings, 2))
# Floor 0: 21.0 C, Floor 1: 25.42 C
```

#### 3D Transformation with Ternary Logic
```python
# Build an alert cube: "ALERT" if reading > 26.0 else "NORMAL"
status_cube = []
for floor in building_temps:
    floor_status = []
    for room in floor:
        room_status = ["ALERT" if t > 26.0 else "NORMAL" for t in room]
        floor_status.append(room_status)
    status_cube.append(floor_status)
```

#### Time Complexity Awareness
- 1D Array Loop: $O(N)$
- 2D Matrix Nested Loop: $O(R \times C)$ (or $O(N^2)$ for square matrices)
- 3D Cube 3-Level Nested Loop: $O(D \times R \times C)$ (or $O(N^3)$ for cubic volumes)

---

## 4. Deep Dive into Python Functions

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
- **Pure Function**: Given identical inputs, always yields identical outputs without altering external state or mutating input objects.
- **Side Effects**: Mutating mutable arguments, modifying global variables, printing to stdout, or performing network/disk I/O.

---

## 5. Variable Scope and The LEGB Rule

When Python resolves a variable name, it traverses four scopes in strict sequence:

```
+-----------------------------------------------------------+
| 1. Local (L): Inside the executing function body          |
+-----------------------------------------------------------+
                             |
                             v
+-----------------------------------------------------------+
| 2. Enclosing (E): Inside enclosing functions / closures    |
+-----------------------------------------------------------+
                             |
                             v
+-----------------------------------------------------------+
| 3. Global (G): Top level of the current module/file       |
+-----------------------------------------------------------+
                             |
                             v
+-----------------------------------------------------------+
| 4. Built-in (B): Python pre-defined builtins (len, range) |
+-----------------------------------------------------------+
```

```python
app_env = "PRODUCTION"  # Global

def outer():
    service_tag = "SVC-AUTH"  # Enclosing
    
    def inner():
        request_id = "REQ-101"  # Local
        print(request_id, service_tag, app_env, len("test"))
        
    inner()
```

### Scope Modifiers: `global` and `nonlocal`
- `global var_name`: Allows modifying a module-level variable inside a local scope.
- `nonlocal var_name`: Allows modifying a variable bound in the nearest enclosing function scope.

---

## 6. Variadic Arguments & Keyword-Only Parameters

### 6.1 `*args` and `**kwargs`
- `*args`: Packs arbitrary extra positional arguments into a **tuple**.
- `**kwargs`: Packs arbitrary extra keyword arguments into a **dictionary**.

```python
def flexible_logger(level: str, *messages, **metadata):
    full_message = " ".join(str(m) for m in messages)
    print(f"[{level.upper()}] {full_message}")
    for k, v in metadata.items():
        print(f"   {k}: {v}")

flexible_logger("info", "User", 101, "logged in", ip="192.168.1.1", os="Linux")
```

### 6.2 Keyword-Only Parameters
Parameters placed after a bare `*` must be passed using explicit keyword syntax:
```python
def configure_cache(timeout: int, *, persistent: bool = False, max_size: int = 1000):
    pass

# Valid
configure_cache(300, persistent=True, max_size=5000)

# Invalid: Raises TypeError
# configure_cache(300, True, 5000)
```

---

## 7. Modern Comprehensions

### 7.1 List Comprehensions
```python
# Standard with filter: [expr for item in seq if cond]
evens_squared = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# With Ternary transformation: [true_val if cond else false_val for item in seq]
labels = ["EVEN" if x % 2 == 0 else "ODD" for x in range(5)]
# ['EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN']
```

### 7.2 2D Nested Comprehensions
```python
# Flattening a 2D matrix into a 1D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [val for row in matrix for val in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generating a 2D multiplication grid
grid_2d = [[r * c for c in range(1, 4)] for r in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### 7.3 Dictionary and Set Comprehensions
```python
# Dictionary Comprehension
names = ["alice", "bob", "charlie"]
name_lengths = {name.title(): len(name) for name in names}
# {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# Set Comprehension (Automatic deduplication)
unique_vowels = {ch for ch in "supercalifragilisticexpialidocious" if ch in "aeiou"}
# {'a', 'e', 'i', 'o', 'u'}
```

---

## 8. Summary & Reference Cheat Sheet

| Construct | Syntax Pattern | Primary Use Case |
| :--- | :--- | :--- |
| `for` Loop | `for item in iterable:` | Definite iteration across sequences or ranges |
| `while` Loop | `while condition:` | Indefinite iteration until condition changes or breaks |
| `enumerate()` | `for idx, val in enumerate(seq, start=0):` | Accessing index along with elements |
| `zip()` | `for a, b in zip(seq_a, seq_b):` | Parallel iteration over multiple sequences |
| Loop `else` | `for ...: break \n else:` | Executed only when loop finishes without `break` |
| Ternary Operator | `val_a if cond else val_b` | Inline conditional expression / value assignment |
| 1D Array Loop | `for x in arr:` / `for i in range(len(arr)):` | Scanning or modifying single-dimension lists |
| 2D Array Loop | `for r in range(R): for c in range(C):` | Traversing matrices, grids, tabular datasets |
| 3D Array Loop | `for z in ...: for y in ...: for x in ...:` | Traversing cubes, layers, batches, sensor grids |
| Variadics | `def f(*args, **kwargs):` | Accepting arbitrary positional and keyword parameters |
| Comprehensions | `[expr for x in seq if cond]` | Concise, declarative creation of lists, dicts, sets |
