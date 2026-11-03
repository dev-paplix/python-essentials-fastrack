# Module 4: String Manipulation

---

## 1. Basics of Handling Text in Python

### What is a String in Python?
A string (`str`) in Python is an **ordered, immutable sequence of Unicode characters**. Because strings are immutable, any operation that modifies a string creates and returns a brand-new string object.

### String Literals and Escape Sequences
```python
single = 'Hello'
double = "World"
multiline = """Line 1
Line 2
Line 3"""

# Common Escape Sequences:
# \n : Newline
# \t : Tab
# \\ : Literal backslash
# \' : Literal single quote
# \" : Literal double quote

# Raw Strings (disables escape sequence interpretation):
regex_pattern = r"C:\new_folder\test.txt" # \n is NOT treated as a newline
```

### String Indexing and Slicing
Python uses zero-based indexing and supports negative indexing from the end:
```
Index:    0   1   2   3   4   5
String:   P   y   t   h   o   n
Neg:     -6  -5  -4  -3  -2  -1
```

**Slicing Syntax**: `string[start : stop : step]`
- `start` (inclusive)
- `stop` (exclusive)
- `step` (stride; negative step reverses the string)

```python
s = "Python Programming"
s[0:6]        # 'Python'
s[:6]         # 'Python' (default start=0)
s[7:]         # 'Programming' (default stop=end)
s[::2]        # 'Pto rgamn' (every 2nd character)
s[::-1]       # 'gnimmargorP nohtyP' (reverses string!)
```

---

## 2. Essential String Methods

Python provides dozens of powerful built-in methods:

| Category | Method | Description | Example |
| :--- | :--- | :--- | :--- |
| **Case Alteration** | `.lower()`, `.upper()` | Converts to lower/upper case | `"Python".lower() -> "python"` |
| | `.title()`, `.capitalize()` | Title-cases or capitalizes first char | `"hello world".title() -> "Hello World"` |
| **Trimming** | `.strip()` | Removes leading/trailing whitespace | `"  hi  ".strip() -> "hi"` |
| | `.lstrip()`, `.rstrip()` | Trims left or right side only | `"--hi--".strip("-") -> "hi"` |
| **Search & Count** | `.find(sub)` | Returns first index or `-1` if not found | `"cat".find("a") -> 1` |
| | `.count(sub)` | Returns number of non-overlapping occurrences | `"banana".count("a") -> 3` |
| | `.startswith(sub)` | Returns boolean | `"report.csv".endswith(".csv") -> True` |
| **Transform & Replace** | `.replace(old, new)` | Replaces occurrences | `"apple".replace("p", "b") -> "abble"` |
| **Splitting & Joining** | `.split(sep)` | Splits into list of strings | `"a,b,c".split(",") -> ['a', 'b', 'c']` |
| | `sep.join(list)` | Joins iterable with separator | `"-".join(['2026', '11', '03']) -> "2026-11-03"` |

---

## 3. String Formatting Evolution

1. **Old C-Style Formatting (`%`)**:
   `"Hello %s, you scored %d" % ("Alice", 95)`
2. **`str.format()` (Python 3.0+)**:
   `"Hello {}, you scored {}".format("Alice", 95)`
3. **Formatted String Literals (f-strings - Python 3.6+) - Industry Standard**:
   ```python
   name = "Alice"
   score = 95.456
   print(f"Student: {name.upper()}, Score: {score:.1f}%")
   # Output: Student: ALICE, Score: 95.5%
   ```

---

## 4. Practical Project: Text Analysis & Data Sanitization

String operations are the foundation of:
- Cleaning messy user input (stripping whitespace, lowercasing emails).
- Creating URL-friendly "slugs" from article titles:
  `"Learn Python in 2026! Fast & Easy" -> "learn-python-in-2026-fast-and-easy"`
- Masking sensitive Personal Identifiable Information (PII) such as credit cards or phone numbers.

