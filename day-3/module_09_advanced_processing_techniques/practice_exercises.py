"""
Module 9: Advanced Processing Techniques - Student Practice Exercises
Course: Python Essentials FastTrack

Instructions:
1. Complete the challenges below.
2. Run this file to verify your solutions against the automated assertions.
"""

import re
import ctypes
import sys

# =====================================================================
# Exercise 1: Custom Exception Hierarchy & Retry Mechanism
# =====================================================================
# Problem Statement:
# Define a custom exception `RateLimitExceeded(Exception)`.
# Then write a function `mock_api_caller(attempts_needed: int) -> str`
# It simulates calling an external API.
# - On each invocation attempt (from 1 up to 3):
#   - If attempt < attempts_needed: raise RateLimitExceeded(f"Rate limited on attempt {attempt}")
#   - If attempt == attempts_needed: return "Payload 200 OK"
# Implement a retry loop inside `execute_with_retry(attempts_needed: int, max_retries: int = 3) -> str`
# that catches `RateLimitExceeded` and retries until success or raises RuntimeError if attempts exceed max_retries.

class RateLimitExceeded(Exception):
    """Raised when an API request is throttled."""
    pass

def execute_with_retry(attempts_needed: int, max_retries: int = 3) -> str:
    """Retries operation up to max_retries upon RateLimitExceeded."""
    for attempt in range(1, max_retries + 1):
        try:
            if attempt < attempts_needed:
                raise RateLimitExceeded(f"Rate limited on attempt {attempt}")
            return "Payload 200 OK"
        except RateLimitExceeded:
            if attempt == max_retries:
                raise RuntimeError("Max retries exceeded")
    raise RuntimeError("Max retries exceeded")


# =====================================================================
# Exercise 2: HTML Table Parser for Web Scraping
# =====================================================================
# Problem Statement:
# Write a function `scrape_table_rows(html: str) -> list`
# Using regex or string parsing, extract all table rows `<tr>...</tr>`
# and within each row, extract table cell text `<td>...</td>`.
# Return a list of lists of strings, trimmed of whitespace.
# Example:
# <tr><td>AAPL</td><td>180.50</td></tr> -> [["AAPL", "180.50"]]

def scrape_table_rows(html: str) -> list:
    """Extract tabular rows and cell contents from HTML."""
    rows = []
    # Find all <tr> tags
    tr_matches = re.findall(r"<tr>(.*?)</tr>", html, flags=re.DOTALL | re.IGNORECASE)
    for tr in tr_matches:
        # Find all <td> tags within row
        td_matches = re.findall(r"<td>(.*?)</td>", tr, flags=re.DOTALL | re.IGNORECASE)
        cleaned_cells = [td.strip() for td in td_matches]
        if cleaned_cells:
            rows.append(cleaned_cells)
    return rows


# =====================================================================
# Exercise 3: Calling C Library String Length via ctypes
# =====================================================================
# Problem Statement:
# Write a function `c_strlen(text: str) -> int`
# Use `ctypes` to invoke the standard C library function `strlen`
# passing the ASCII encoded bytes of `text`, and return the integer length.

def c_strlen(text: str) -> int:
    """Invokes compiled C runtime strlen function."""
    if sys.platform == "win32":
        libc = ctypes.cdll.msvcrt
    else:
        libc = ctypes.CDLL("libc.so.6")
        
    libc.strlen.argtypes = [ctypes.c_char_p]
    libc.strlen.restype = ctypes.c_size_t
    
    encoded_bytes = text.encode("utf-8")
    return int(libc.strlen(encoded_bytes))


# =====================================================================
# Verification Test Suite
# =====================================================================
def run_tests():
    print("=" * 60)
    print("RUNNING MODULE 9 PRACTICE TESTS")
    print("=" * 60)

    # Test Exercise 1
    res = execute_with_retry(attempts_needed=2, max_retries=3)
    assert res == "Payload 200 OK"
    
    try:
        execute_with_retry(attempts_needed=5, max_retries=3)
        assert False, "Should have raised RuntimeError"
    except RuntimeError as e:
        assert "Max retries exceeded" in str(e)
    print("  [PASS] Exercise 1: Custom Exception & Retry works correctly!")

    # Test Exercise 2
    html_sample = """
    <table>
        <tr>
            <th>Ticker</th>
            <th>Price</th>
        </tr>
        <tr>
            <td>MSFT</td>
            <td> 410.25 </td>
        </tr>
        <tr>
            <td>GOOGL</td>
            <td>175.80</td>
        </tr>
    </table>
    """
    rows = scrape_table_rows(html_sample)
    assert len(rows) == 2
    assert rows[0] == ["MSFT", "410.25"]
    assert rows[1] == ["GOOGL", "175.80"]
    print("  [PASS] Exercise 2: HTML Table Parser works correctly!")

    # Test Exercise 3
    sample_str = "GemRain FastTrack"
    c_len = c_strlen(sample_str)
    assert c_len == len(sample_str) == 17, f"Expected 17, got {c_len}"
    print(f"  [PASS] Exercise 3: C Runtime strlen via ctypes works correctly! (Length={c_len})")

    print("\nAll Module 9 exercises passed successfully! Outstanding work!\n")

if __name__ == "__main__":
    run_tests()

