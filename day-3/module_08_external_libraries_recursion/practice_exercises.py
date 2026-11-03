"""
Module 8: Practical Application & External Libraries - Student Practice Exercises
Course: Python Essentials FastTrack

Instructions:
1. Complete each challenge below.
2. Run this script to test your solutions against the automated assertions.
"""

import json
import base64

# =====================================================================
# Exercise 1: Recursive Nested Dictionary Key Search
# =====================================================================
# Problem Statement:
# In complex configuration files or API responses, keys are often deeply nested.
# Write a recursive function `find_nested_value(data: dict, target_key: str)`
# Search through `data` (and any dictionaries nested inside it).
# Return the first value matching `target_key`, or None if not found.

def find_nested_value(data: dict, target_key: str):
    """Recursively search for a key in a nested dictionary."""
    if not isinstance(data, dict):
        return None
        
    if target_key in data:
        return data[target_key]
        
    for val in data.values():
        if isinstance(val, dict):
            found = find_nested_value(val, target_key)
            if found is not None:
                return found
        elif isinstance(val, list):
            for item in val:
                if isinstance(item, dict):
                    found = find_nested_value(item, target_key)
                    if found is not None:
                        return found
                        
    return None


# =====================================================================
# Exercise 2: Base64 JSON Stream Serializer & Deserializer
# =====================================================================
# Problem Statement:
# Write two functions:
# 1. `encode_payload(payload: dict) -> str`
#    Converts a Python dict to a JSON string and encodes it as an ASCII Base64 string.
# 2. `decode_payload(encoded_str: str) -> dict`
#    Decodes an ASCII Base64 string back into the original Python dictionary.

def encode_payload(payload: dict) -> str:
    """Serializes dict to JSON then Base64 encodes it."""
    json_bytes = json.dumps(payload).encode("utf-8")
    return base64.b64encode(json_bytes).decode("ascii")

def decode_payload(encoded_str: str) -> dict:
    """Decodes Base64 string and parses JSON to dict."""
    decoded_bytes = base64.b64decode(encoded_str.encode("ascii"))
    return json.loads(decoded_bytes.decode("utf-8"))


# =====================================================================
# Exercise 3: Financial Stock Volatility & Moving Average
# =====================================================================
# Problem Statement:
# Write `compute_stock_metrics(prices: list, window: int = 3) -> dict`
# Given a list of daily closing prices:
# - "high": Highest price in series
# - "low": Lowest price in series
# - "rolling_averages": List of rolling averages with size `window` (first window-1 items are None).
#   Each valid average rounded to 2 decimal places.
# - "overall_change_pct": Percentage change from first to last price ((last - first) / first * 100), rounded to 2 decimals.

def compute_stock_metrics(prices: list, window: int = 3) -> dict:
    """Computes high, low, rolling averages, and overall % change for stock prices."""
    if not prices:
        return {}
        
    rolling = []
    for i in range(len(prices)):
        if i + 1 < window:
            rolling.append(None)
        else:
            subset = prices[i + 1 - window : i + 1]
            rolling.append(round(sum(subset) / window, 2))
            
    pct_change = ((prices[-1] - prices[0]) / prices[0]) * 100
    
    return {
        "high": max(prices),
        "low": min(prices),
        "rolling_averages": rolling,
        "overall_change_pct": round(pct_change, 2)
    }


# =====================================================================
# Verification Test Suite
# =====================================================================
def run_tests():
    print("=" * 60)
    print("RUNNING MODULE 8 PRACTICE TESTS")
    print("=" * 60)

    # Test Exercise 1
    config = {
        "app": {
            "name": "CloudPlatform",
            "database": {
                "connection": {
                    "port": 5432,
                    "credentials": {
                        "api_secret": "SEC-88219"
                    }
                }
            }
        }
    }
    assert find_nested_value(config, "api_secret") == "SEC-88219"
    assert find_nested_value(config, "port") == 5432
    assert find_nested_value(config, "non_existent") is None
    print("  [PASS] Exercise 1: Recursive Nested Dict Search works correctly!")

    # Test Exercise 2
    original = {"client": "GemRain", "seats": 25, "active": True}
    encoded = encode_payload(original)
    assert isinstance(encoded, str)
    decoded = decode_payload(encoded)
    assert decoded == original
    print("  [PASS] Exercise 2: Base64 JSON Stream Encoder/Decoder works correctly!")

    # Test Exercise 3
    daily_quotes = [100.0, 102.0, 104.0, 108.0, 110.0]
    metrics = compute_stock_metrics(daily_quotes, window=3)
    assert metrics["high"] == 110.0
    assert metrics["low"] == 100.0
    assert metrics["rolling_averages"] == [None, None, 102.0, 104.67, 107.33]
    assert metrics["overall_change_pct"] == 10.0
    print("  [PASS] Exercise 3: Stock Metrics & Moving Average works correctly!")

    print("\nAll Module 8 exercises passed successfully! Outstanding work!\n")

if __name__ == "__main__":
    run_tests()

