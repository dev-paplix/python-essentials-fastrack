# Module 9: Advanced Processing Techniques

---

## 1. Optical Character Recognition (OCR)

### What is OCR?
Optical Character Recognition (OCR) is the computational process of detecting, segmenting, and transcribing text contained within pixel-based images (scanned documents, photos, PDF snapshots) into machine-readable Unicode strings.

### The Modern Python OCR Pipeline
```
┌──────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐      ┌──────────────────┐
│   Input Image    │ ───► │  Preprocessing (Pillow) │ ───► │     OCR Engine (Tesseract)│ ───► │ Extracted Text   │
│ (PNG, JPG, TIFF) │      │ Grayscale, Binarize     │      │   Feature Extraction    │      │  (Unicode str)   │
└──────────────────┘      └─────────────────────────┘      └─────────────────────────┘      └──────────────────┘
```

1. **Preprocessing (PIL / Pillow)**:
   - Convert image to grayscale (`.convert('L')`).
   - Binarization (thresholding) to isolate high-contrast text from noisy backgrounds.
2. **Recognition Engine (`pytesseract`)**:
   - Google's open-source Tesseract OCR engine processes image arrays and outputs decoded strings.

```python
# Typical production OCR invocation:
from PIL import Image
# import pytesseract

def extract_receipt_text(image_path: str) -> str:
    # img = Image.open(image_path)
    # text = pytesseract.image_to_string(img)
    # return text
    pass
```

---

## 2. Integrating External C Libraries (`ctypes`)

### Why Call C from Python?
While Python delivers rapid development speed, certain computational tasks (cryptography, signal processing, legacy kernel/system drivers) demand raw hardware performance. Python's built-in `ctypes` library provides a **Foreign Function Interface (FFI)** to call functions directly inside compiled C shared libraries (`.dll` on Windows, `.so` on Linux, `.dylib` on macOS).

### Mapping Types Between C and Python

| Python Type | `ctypes` Type | Equivalent C Type |
| :--- | :--- | :--- |
| `int` | `ctypes.c_int` | `int` |
| `float` | `ctypes.c_double` | `double` |
| `str` / `bytes` | `ctypes.c_char_p` | `char *` (pointer to null-terminated string) |
| `None` | `ctypes.c_void_p` | `void *` (null pointer) |

### Loading C Libraries & Configuring Signatures
```python
import ctypes
import os

# On Windows: Load the standard C runtime library (msvcrt)
libc = ctypes.cdll.msvcrt

# 1. Calling standard C functions (e.g., puts)
libc.puts.argtypes = [ctypes.c_char_p]
libc.puts.restype = ctypes.c_int
libc.puts(b"Hello directly from compiled C runtime!")

# 2. Calling C math functions (e.g., sqrt, pow)
libc.sqrt.argtypes = [ctypes.c_double]
libc.sqrt.restype = ctypes.c_double
result = libc.sqrt(ctypes.c_double(144.0))
print(f"C sqrt result: {result}")
```

---

## 3. Advanced String Formatting with F-Strings

Python 3.6+ introduced f-strings, with advanced features refined in 3.8+:

```python
# 1. Number Formatting & Alignment
value = 1234567.891
print(f"{value:,.2f}")      # '1,234,567.89' (comma grouped, 2 decimal places)
print(f"{value:>20.2f}")     # Right aligned in 20-character field
print(f"{value:<20.2f}")     # Left aligned
print(f"{'TITLE':^20}")      # Center aligned: '       TITLE        '

# 2. Base Representations
num = 255
print(f"Hex: {num:#x}, Octal: {num:#o}, Binary: {num:#b}")
# Hex: 0xff, Octal: 0o377, Binary: 0b11111111

# 3. Inline Debug Expressions (Python 3.8+)
x = 42
y = 100
print(f"{x=}, {y=}, {x+y=}") # Outputs: x=42, y=100, x+y=142
```

---

## 4. Web Scraping Essentials

Web scraping automates data harvesting from HTML websites:
1. **Target Identification**: Inspecting DOM elements, tag attributes (`class`, `id`).
2. **HTTP Retrieval**: Sending headers with a legitimate `User-Agent` to avoid being blocked.
3. **DOM Parsing**: Extracting structured tables, links, and text using `BeautifulSoup` or standard regex/HTML parsers.
4. **Scraping Ethics**: Respect `robots.txt`, implement request throttling (delays between calls), and never hammer production servers.

---

## 5. Robust Error Handling and Custom Exceptions

### The Python Exception Hierarchy
```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception (Standard root for application errors)
      ├── ArithmeticError (ZeroDivisionError, OverflowError)
      ├── LookupError (IndexError, KeyError)
      ├── TypeError
      └── ValueError
```

### The Full `try-except-else-finally` Block
```python
try:
    file = open("data.json", "r")
    payload = json.load(file)
except FileNotFoundError:
    print("File was missing!")
except json.JSONDecodeError as err:
    print(f"Corrupt JSON payload: {err}")
else:
    # Runs ONLY if NO exceptions were raised in try block
    print("Data parsed cleanly!")
finally:
    # ALWAYS runs, regardless of success or unhandled exception
    print("Cleaning up resources.")
```

### Creating Custom Enterprise Exceptions
```python
class BankingException(Exception):
    """Base exception for all banking operations."""
    pass

class InsufficientFundsError(BankingException):
    def __init__(self, balance: float, withdrawal: float):
        self.balance = balance
        self.withdrawal = withdrawal
        super().__init__(f"Cannot withdraw ${withdrawal:.2f}. Available balance: ${balance:.2f}")
```

