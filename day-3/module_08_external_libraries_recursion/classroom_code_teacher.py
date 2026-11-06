import sys
import json
import base64
import io
import urllib.request
import urllib.error


def header(title):
    print(f"\n" + "=" * 70)
    print(title)
    print("=" * 70)

# Recursion and External Libraries
header("External Libraries and Recursion and Mechanics of Python")

def recursive_sum(numbers: list) -> int:
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

def flatten_nested_list(nested_list: list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_nested_list(item))
        else:
            flat_list.append(item)
    return flat_list

sample_nested_list = [1, [2, 3], [[4, [5, 6]], 7], 8]
print(f"Original nested list: {sample_nested_list}")
print(f"Flattened list: {flatten_nested_list(sample_nested_list)}")

#Base64, JSON, and IO
header("Data Stream Conversion: Base64, JSON, and IO")

order_data ={
    "order_id": "ORD-2026-1705",
    "customer": "Gemrain Sdn Bhd",
    "items": [
        {"item_id": "ITEM-001", "name": "Acer Aspire", "quantity": 2, "price": 4580.0},
        {"item_id": "ITEM-002", "name": "MacBook Pro", "quantity": 1, "price": 7425.0}
    ],
    "is_paid": True,
}

# Serialize to JSON
json_data = json.dumps(order_data, indent=2)
print(f"Serialized JSON:\n{json_data}")

# Encode to Base64 for security and transmission
raw_bytes = json_data.encode('utf-8')
base64_bytes = base64.b64encode(raw_bytes).decode("ascii")
print(f"\nBase64 Encoded Data:\n{base64_bytes}")

# Decode from Base64 back to Python dict
decoded_bytes = base64.b64decode(base64_bytes.encode("ascii"))
decoded_dict = json.loads(decoded_bytes.decode("utf-8"))
print(f"\nDecoded Dictionary:\n{decoded_dict['customer']}")

# IO for Memory Stream
buffer = io.StringIO()
buffer.write("\nLog Header: Stream Started\n")
buffer.write("Payload received successfully\n")
buffer.seek(0)
print(f"\nMemory Stream Content:\n{buffer.read().strip()}")

# Using urllib to fetch data from a URL for API
header("Fetching Data from URL using urllib")
# Realtime Bitcoin Price API : https://coingecko.com

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    headers = {"User-Agent": "Mozilla/5.0", "accept": "application/json"}

    try:
        # Send GET request with a 10-second server timeout limit
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            # Read and decode response body, then parse JSON
            raw_data = response.read().decode("utf-8")
            data = json.loads(raw_data)
        
        print("Successfully connected to CoinGecko Public API!")
        print(f"Bitcoin: ${data['bitcoin']['usd']:,} USD")
        print(f"Ethereum: ${data['ethereum']['usd']:,} USD")

    except urllib.error.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err.code} - {http_err.reason}")
    except urllib.error.URLError as url_err:
        print(f"Network error: Could not reach the server ({url_err.reason})")
    except json.JSONDecodeError as json_err:
        print(f"Failed to parse JSON response: {json_err}")
    except Exception as err:
        print(f"An unexpected script error occurred: {err}")

fetch_bitcoin_price()
