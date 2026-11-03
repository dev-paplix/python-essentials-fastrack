# Module 11: New Features in Python 3.10 and 3.11

---

## 1. Structural Pattern Matching: Python's 'Switch' Statement (PEP 634)

Introduced in **Python 3.10**, Structural Pattern Matching provides Python with a feature far superior to traditional `switch/case` statements found in C or Java. It matches not just primitive values, but **the shape, type, and contents** of data structures.

### Syntax Anatomy
```python
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2> if <guard_condition>:
        <action_2>
    case _:
        <default_wildcard_fallback>
```

### 1. Literal and OR Patterns
```python
http_code = 404

match http_code:
    case 200 | 201:
        print("Success")
    case 400 | 401 | 403:
        print("Client Error")
    case 404:
        print("Not Found")
    case 500 | 502 | 503:
        print("Server Infrastructure Error")
    case _:
        print("Unknown Status Code")
```

### 2. Sequence Patterns (Unpacking Lists and Tuples)
```python
command = ["move", 10, 20]

match command:
    case ["quit"]:
        terminate()
    case ["move", x, y]:
        update_position(x, y)
    case ["scale", factor]:
        resize(factor)
    case ["draw", shape, *coordinates]:
        render(shape, coordinates)
    case _:
        print("Unrecognized command syntax")
```

### 3. Mapping Patterns & Guard Clauses
```python
event = {"type": "click", "button": "left", "x": 120, "y": 80}

match event:
    case {"type": "click", "button": "left", "x": x, "y": y} if x < 200:
        print(f"Left clicked inside sidebar navigation at ({x}, {y})")
    case {"type": "click", "button": btn}:
        print(f"Other button clicked: {btn}")
    case {"type": "hover"}:
        print("Mouse hovering")
    case _:
        print("Other event")
```

---

## 2. Python 3.11 CPython Optimizations

Python 3.11 introduced major architectural speed enhancements as part of the **Faster CPython Project**:

### 1. Specialized Adaptive Interpreter (PEP 659)
In Python 3.11, the interpreter observes running bytecode. When an operation (such as attribute access or binary addition) repeatedly receives the same data types, bytecode is dynamically specialized in-place (e.g., replacing generic `LOAD_ATTR` with monomorphic `LOAD_ATTR_SLOT` or `LOAD_ATTR_MODULE`). This yields an average **25% speed improvement** over Python 3.10 out of the box with zero code changes!

### 2. Zero-Cost Exceptions
In previous versions, `try-except` blocks carried a minor runtime execution overhead. In Python 3.11, `try` blocks incur zero overhead during normal execution; costs are only paid when an exception is actually raised.

### 3. Pinpoint Precise Tracebacks
Python 3.11 highlights the exact token and expression range that failed:
```text
Traceback (most recent call last):
  File "calc.py", line 12, in <module>
    result = calculate(data["user"]["profile"]["age"])
                       ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^
KeyError: 'age'
```

---

## 3. Advanced F-String Features

### Self-Documenting Expressions (`{expr=}`)
Added in Python 3.8 and refined in 3.10+:
```python
import math
theta = math.pi / 4
print(f"{theta=:.4f}, {math.sin(theta)=:.4f}")
# Output: theta=0.7854, math.sin(theta)=0.7071
```

### Nested Format Specifications
Dynamically control padding, width, and decimal precision:
```python
value = 123.456789
width = 12
precision = 3
print(f"[{value:{width}.{precision}f}]") # '[     123.457]'
```

---

## 4. I/O Parallelization Techniques

Python programs spend significant time waiting on **I/O** (network sockets, disk read/writes, database queries). Parallelizing these operations drastically improves throughput.

### ThreadPoolExecutor vs Asyncio

| Concurrency Model | Best For | Typical Use Cases |
| :--- | :--- | :--- |
| **`ThreadPoolExecutor`** | Preemptive multitasking across blocking I/O calls | Downloading dozens of URLs, scraping multiple pages, parallel disk reads |
| **`ProcessPoolExecutor`** | True multi-core parallelism for CPU-bound computation | Image resizing, cryptography, machine learning training |
| **`asyncio`** | Cooperative, single-threaded event loop | High-concurrency servers handling 10,000+ persistent sockets (FastAPI, WebSockets) |

### ThreadPoolExecutor Example
```python
from concurrent.futures import ThreadPoolExecutor
import time

def fetch_url(url: str) -> str:
    # Simulates I/O network latency
    time.sleep(1.0)
    return f"Contents of {url}"

urls = [f"https://service.org/api/v1/item/{i}" for i in range(10)]

# Serial takes ~10 seconds.
# Parallel with 5 workers takes only ~2 seconds!
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_url, urls))
```

