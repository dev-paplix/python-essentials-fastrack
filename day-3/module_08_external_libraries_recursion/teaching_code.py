"""
Module 8: Practical Application & External Libraries - Teaching Code
Instructor Demonstration Script
Course: Python Essentials FastTrack
"""

import sys
import json
import base64
import io
import urllib.request
import urllib.error

def header(title: str):
    print("\n" + "=" * 60)
    print(f" {title.upper()} ")
    print("=" * 60)

# =====================================================================
# 1. Recursion Mechanics & Stack Tree
# =====================================================================
header("1. Recursion: Call Stack and Flattening Nested Data")

def recursive_sum(numbers: list) -> int:
    """Computes sum of list recursively."""
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

def flatten_nested_list(nested: list) -> list:
    """
    Recursively flattens arbitrarily nested lists.
    E.g.: [1, [2, [3, 4], 5], 6] -> [1, 2, 3, 4, 5, 6]
    """
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_nested_list(item))
        else:
            flat.append(item)
    return flat

sample_nested = [1, [2, 3], [[4, [5, 6]], 7], 8]
print(f"Original nested structure: {sample_nested}")
print(f"Recursively flattened   : {flatten_nested_list(sample_nested)}")

# =====================================================================
# 2. Data Stream Conversions: JSON, Base64 & BytesIO
# =====================================================================
header("2. Data Stream Conversion: JSON & Base64")

order_record = {
    "order_id": "ORD-2026-9981",
    "customer": "TechCorp Asia",
    "items": [{"sku": "SRV-RACK", "qty": 2, "price": 1450.00}],
    "is_settled": True
}

# 1. Serialization: Dict to JSON string
json_stream = json.dumps(order_record, indent=2)
print("Serialized JSON stream:")
print(json_stream)

# 2. Encoding to Base64 for transport
raw_bytes = json_stream.encode("utf-8")
base64_encoded = base64.b64encode(raw_bytes).decode("ascii")
print(f"\nBase64 Encoded Stream:\n{base64_encoded}")

# 3. Decoding back from Base64 to Python Dict
recovered_bytes = base64.b64decode(base64_encoded.encode("ascii"))
recovered_dict = json.loads(recovered_bytes.decode("utf-8"))
print(f"\nRecovered Order ID: {recovered_dict['order_id']}")

# In-Memory Stream Buffer (io.StringIO)
buffer = io.StringIO()
buffer.write("Log Header: Stream started\n")
buffer.write("Payload received successfully\n")
buffer.seek(0)
print(f"\nReading from in-memory stream:\n{buffer.read().strip()}")

# =====================================================================
# 3. Data Acquisition via HTTP REST API
# =====================================================================
header("3. REST API Data Acquisition (HTTP GET)")

def fetch_public_api_data():
    """Fetches real-time cryptocurrency quote from public API with fallback."""
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    req = urllib.request.Request(url, headers={"User-Agent": "PythonFastTrack"})
    
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            bpi = data["bpi"]["USD"]
            print(f"Live BTC/USD Rate: ${bpi['rate_float']:,.2f} ({bpi['description']})")
    except Exception as e:
        print(f"Network call skipped or offline ({e}). Using simulated API payload.")
        simulated = {"code": "USD", "rate": 65420.50}
        print(f"Simulated BTC/USD Rate: ${simulated['rate']:,.2f}")

fetch_public_api_data()

# =====================================================================
# 4. Project: Historical Stock Data Analytics & Moving Averages
# =====================================================================
header("4. Historical Stock Analytics & ASCII Overview")

class StockAnalyzer:
    def __init__(self, ticker: str, historical_prices: list):
        self.ticker = ticker
        self.prices = historical_prices

    def calculate_sma(self, window_size: int = 5) -> list:
        """Calculates Simple Moving Average (SMA)."""
        sma_values = []
        for i in range(len(self.prices)):
            if i + 1 < window_size:
                sma_values.append(None)
            else:
                window = self.prices[i + 1 - window_size : i + 1]
                avg = sum(window) / window_size
                sma_values.append(round(avg, 2))
        return sma_values

    def display_ascii_trend(self):
        """Displays terminal graphic trend chart."""
        min_p = min(self.prices)
        max_p = max(self.prices)
        spread = max(1.0, max_p - min_p)
        
        print(f"\nHistorical Price Trend for {self.ticker} (Range: ${min_p:.2f} - ${max_p:.2f}):")
        for idx, price in enumerate(self.prices, start=1):
            bar_len = int(((price - min_p) / spread) * 30)
            bar = "#" * bar_len
            print(f"Day {idx:>2} [${price:>6.2f}]: |{bar:<30}|")

# Simulated 14 days of stock closing prices for AAPL
simulated_stock_data = [150.2, 151.8, 153.4, 152.1, 155.0, 157.3, 156.8, 159.2, 161.0, 160.5, 162.4, 165.1, 164.0, 166.5]
analyzer = StockAnalyzer("AAPL", simulated_stock_data)
analyzer.display_ascii_trend()

sma_5 = analyzer.calculate_sma(5)
print(f"\n5-Day Moving Averages: {sma_5[-5:]}")

if __name__ == "__main__":
    print("\n[SUCCESS] Module 8 Teaching Code executed successfully!")

