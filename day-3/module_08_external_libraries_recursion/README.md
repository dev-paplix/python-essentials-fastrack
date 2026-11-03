# Module 8: Practical Application and External Libraries

---

## 1. Implementing Recursion

### Anatomy of a Recursive Function
A recursive function is a function that calls itself to solve smaller sub-problems of the same type. Every valid recursive algorithm requires two components:
1. **The Base Case**: A terminating condition that stops recursion and returns a direct answer without further self-calls.
2. **The Recursive Step**: Progressing towards the base case by calling itself with smaller or simplified parameters.

```python
def factorial(n: int) -> int:
    # Base Case
    if n <= 1:
        return 1
    # Recursive Step
    return n * factorial(n - 1)
```

### The Call Stack and Recursion Depth
Every recursive invocation pushes a new stack frame onto the Python call stack.
Python guards against infinite stack overflow using a recursion limit (default: 1000 frames):
```python
import sys
print(sys.getrecursionlimit()) # 1000
# Can be queried or adjusted with sys.setrecursionlimit()
```

---

## 2. Data Stream Conversion Techniques

Real-world applications constantly convert data streams across different serialization formats:
- **JSON (JavaScript Object Notation)**: Standard web API format (`json.loads()`, `json.dumps()`).
- **Base64 Encoding**: Converting binary streams (e.g. image bytes, security certificates) into ASCII text for transport over text protocols (`base64.b64encode()`).
- **In-Memory Byte Streams**: Using `io.BytesIO` and `io.StringIO` to treat binary buffers or strings as readable/writable file streams.

```python
import json
import base64

payload = {"stock": "AAPL", "price": 182.50}
# Serialize to JSON string
json_str = json.dumps(payload)

# Encode to Base64 ASCII bytes
encoded = base64.b64encode(json_str.encode("utf-8"))
print(f"Base64 stream: {encoded.decode('ascii')}")
```

---

## 3. Data Acquisition Methods

### HTTP Requests and REST APIs
Modern software interacts with third-party web services through HTTP verbs:
- `GET`: Retrieve resources.
- `POST`: Create new resources or submit forms.
- `PUT` / `PATCH`: Update resources.
- `DELETE`: Remove resources.

Using Python's standard library `urllib.request` or the industry standard `requests` library:
```python
import urllib.request
import json

url = "https://api.github.com"
req = urllib.request.Request(url, headers={"User-Agent": "PythonFastTrack"})
with urllib.request.urlopen(req) as response:
    raw_data = response.read().decode("utf-8")
    data = json.loads(raw_data)
    print(f"API Current User URL: {data.get('current_user_url')}")
```

---

## 4. External Libraries & Virtual Environments (`pip`)
External libraries from PyPI (Python Package Index) can be installed cleanly:
```bash
pip install requests matplotlib pandas yfinance
```

---

## 5. Practical Project: Historical Stock Data Extraction & Analytics
Financial systems extract historical time-series quotes and compute moving averages:
- **Simple Moving Average (SMA)**: The average closing price over a rolling window of $N$ days:
  $$\text{SMA}_k = \frac{1}{N} \sum_{i=0}^{N-1} P_{k-i}$$
- **Price Volatility**: Measuring the standard deviation of percentage daily returns.
- **ASCII / Graphical Visualizations**: Rendering trend overviews directly in terminal or charts.

