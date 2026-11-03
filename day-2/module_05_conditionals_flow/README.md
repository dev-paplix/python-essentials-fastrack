# Module 5: Conditional Logic and Flow Control

---

## 1. Understanding Booleans and Comparison Operators

### Boolean Values & Expressions
Python's `bool` type has only two possible instances: `True` and `False`. Any expression evaluated inside an `if` statement evaluates to a boolean context.

### Comparison Operators

| Operator | Meaning | Example | Result |
| :---: | :--- | :---: | :---: |
| `==` | Value equality | `5 == 5.0` | `True` |
| `!=` | Value inequality | `5 != 3` | `True` |
| `>` | Greater than | `10 > 2` | `True` |
| `<` | Less than | `7 < 1` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `4 <= 5` | `True` |

### Critical Distinction: `==` (Equality) vs `is` (Identity)
- **`==` checks value equality**: Do the two objects represent the same data?
- **`is` checks identity**: Do the two variables point to the exact same object in memory (`id(a) == id(b)`)?

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2) # True (identical content)
print(list1 is list2) # False (different heap memory allocations!)

# Best Practice: Always use 'is' when checking for None or booleans:
if user is None:
    pass
```

---

## 2. Implementing 'if' Statements

### Syntax Hierarchy
```python
if condition_1:
    # Executes when condition_1 is True
    handle_condition_1()
elif condition_2:
    # Executes when condition_1 is False AND condition_2 is True
    handle_condition_2()
else:
    # Fallback when all above conditions are False
    handle_fallback()
```

### The Ternary Operator (Conditional Expression)
Python provides an inline expression for quick conditional assignments:
```python
# syntax: value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"
```

### Clean Code: Guard Clauses over Deep Nesting
Avoid the "Arrow Anti-Pattern" (excessively nested `if` blocks):
```python
# POOR DESIGN:
def process_order(order):
    if order is not None:
        if order.is_paid:
            if order.in_stock:
                ship(order)

# CLEAN DESIGN (Guard Clauses):
def process_order(order):
    if order is None:
        return "Invalid Order"
    if not order.is_paid:
        return "Payment Pending"
    if not order.in_stock:
        return "Out of Stock"
    
    ship(order)
    return "Shipped"
```

---

## 3. Logical Operators and Short-Circuit Evaluation

Python has three logical operators: `and`, `or`, and `not`.

### Short-Circuit Evaluation
Python evaluates compound logical statements lazily from left to right:
- **`and` Short-Circuit**: If the first operand evaluates to `False`, Python immediately returns `False` without evaluating the second operand.
- **`or` Short-Circuit**: If the first operand evaluates to `True`, Python immediately returns `True` without evaluating the second operand.

```python
# Short-circuit prevents ZeroDivisionError!
count = 0
total = 100

if count > 0 and (total / count) > 10:
    print("Sufficient average")
else:
    print("Safe: division was skipped!")
```

### The Return Value of `and` and `or`
In Python, `or` returns the **first truthy value**, or the last value if none are truthy:
```python
# Default value fallback pattern:
user_name = input_name or "Anonymous"
```
And `and` returns the **first falsy value**, or the last value if all are truthy:
```python
result = [1, 2] and "Success" # Returns "Success"
result = [] and "Success"     # Returns []
```

---

## 4. Coding Challenges & Quizzes
Key scenarios implemented in this module:
1. **Tiered Pricing / Progressive Tax Bracket**: Applying conditional rate scales.
2. **Role-Based Access Control (RBAC)**: Validating permissions and role hierarchies.
3. **Password Security Strength Evaluator**: Multi-factor boolean verification.

