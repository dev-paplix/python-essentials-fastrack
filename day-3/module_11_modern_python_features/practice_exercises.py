"""
Module 11: Modern Python Features (3.10 & 3.11) - Student Practice Exercises
Course: Python Essentials FastTrack

Instructions:
1. Complete the challenges below utilizing Python 3.10 match-case and parallel executors.
2. Run this file to verify your solutions against the automated assertions.
"""

from concurrent.futures import ThreadPoolExecutor
import time

# =====================================================================
# Exercise 1: Structural Pattern Matching - REST API Router
# =====================================================================
# Problem Statement:
# Write a function `route_request(method: str, path: str, body: dict = None) -> tuple`
# Implement routing using a `match (method.upper(), path.strip("/").split("/")): ...`
# Rules:
# - ("GET", ["users"]): return (200, "User List")
# - ("GET", ["users", user_id]): return (200, f"Details for user {user_id}")
# - ("POST", ["users"]) if body and "name" in body: return (201, f"Created {body['name']}")
# - ("POST", ["users"]): return (400, "Missing required 'name' field")
# - ("DELETE", ["users", user_id]): return (204, f"Deleted user {user_id}")
# - Wildcard fallback: return (404, "Endpoint Not Found")

def route_request(method: str, path: str, body: dict = None) -> tuple:
    """Dispatches HTTP requests using structural pattern matching."""
    segments = [seg for seg in path.strip("/").split("/") if seg]
    
    match (method.upper(), segments):
        case ("GET", ["users"]):
            return (200, "User List")
            
        case ("GET", ["users", user_id]):
            return (200, f"Details for user {user_id}")
            
        case ("POST", ["users"]) if body and "name" in body:
            return (201, f"Created {body['name']}")
            
        case ("POST", ["users"]):
            return (400, "Missing required 'name' field")
            
        case ("DELETE", ["users", user_id]):
            return (204, f"Deleted user {user_id}")
            
        case _:
            return (404, "Endpoint Not Found")


# =====================================================================
# Exercise 2: Parallel Batch Computation with ThreadPoolExecutor
# =====================================================================
# Problem Statement:
# Given a list of items and a simulated worker function `fetch_item_price(item_id: int) -> float`:
# Write `parallel_fetch_prices(item_ids: list, max_workers: int = 4) -> dict`
# It should query all item IDs concurrently using ThreadPoolExecutor
# and return a dictionary mapping `item_id` to its price.

def fetch_item_price(item_id: int) -> float:
    """Simulated network lookup for an item price."""
    time.sleep(0.05)
    return round(10.0 + (item_id * 1.5), 2)

def parallel_fetch_prices(item_ids: list, max_workers: int = 4) -> dict:
    """Fetch item prices concurrently across worker threads."""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Map returns results in the original order of item_ids
        prices = list(executor.map(fetch_item_price, item_ids))
    return dict(zip(item_ids, prices))


# =====================================================================
# Verification Test Suite
# =====================================================================
def run_tests():
    print("=" * 60)
    print("RUNNING MODULE 11 PRACTICE TESTS")
    print("=" * 60)

    # Test Exercise 1
    assert route_request("GET", "/users") == (200, "User List")
    assert route_request("GET", "/users/42") == (200, "Details for user 42")
    assert route_request("POST", "/users", {"name": "Alice"}) == (201, "Created Alice")
    assert route_request("POST", "/users", {}) == (400, "Missing required 'name' field")
    assert route_request("DELETE", "/users/99") == (204, "Deleted user 99")
    assert route_request("GET", "/unknown/route") == (404, "Endpoint Not Found")
    print("  [PASS] Exercise 1: Structural Pattern Matching Router works correctly!")

    # Test Exercise 2
    test_ids = [1, 2, 3, 4, 5]
    start = time.time()
    prices = parallel_fetch_prices(test_ids, max_workers=5)
    elapsed = time.time() - start
    
    assert len(prices) == 5
    assert prices[1] == 11.5
    assert prices[5] == 17.5
    # Since 5 tasks run concurrently each taking 0.05s, total time should be << 0.25s
    assert elapsed < 0.20, f"Expected concurrency under 0.20s, got {elapsed:.2f}s"
    print(f"  [PASS] Exercise 2: Parallel Fetching works correctly! (Elapsed: {elapsed:.3f}s)")

    print("\nAll Module 11 exercises passed successfully! Outstanding work!\n")

if __name__ == "__main__":
    run_tests()

