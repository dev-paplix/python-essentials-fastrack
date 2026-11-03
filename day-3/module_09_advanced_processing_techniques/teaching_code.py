"""
Module 9: Advanced Processing Techniques - Teaching Code
Instructor Demonstration Script
Course: Python Essentials FastTrack
"""

import sys
import ctypes
import re
from html.parser import HTMLParser

def header(title: str):
    print("\n" + "=" * 60)
    print(f" {title.upper()} ")
    print("=" * 60)

# =====================================================================
# 1. Optical Character Recognition (OCR) Pipeline Simulation
# =====================================================================
header("1. Optical Character Recognition (OCR) Architecture")

class ReceiptOCRProcessor:
    """
    Demonstrates image text extraction and parser pipeline.
    In production environments, uses pytesseract / EasyOCR.
    """
    def __init__(self, raw_ocr_output: str):
        self.raw_text = raw_ocr_output

    def parse_receipt(self) -> dict:
        """Parses vendor, date, and line item amounts from OCR text."""
        lines = [line.strip() for line in self.raw_text.strip().split("\n") if line.strip()]
        vendor = lines[0] if lines else "UNKNOWN"
        
        # Regex to locate amounts e.g. $19.99 or 45.00
        amount_matches = re.findall(r"\$?\s*(\d+\.\d{2})", self.raw_text)
        amounts = [float(a) for a in amount_matches]
        
        total = max(amounts) if amounts else 0.0
        return {
            "vendor": vendor,
            "detected_amounts": amounts,
            "extracted_total": total
        }

simulated_ocr_text = """
GEMRAIN RESTAURANT SDN BHD
Date: 2026-11-03
1x Americano      $ 12.50
1x Avocado Toast  $ 28.00
Subtotal          $ 40.50
Tax (6%)          $  2.43
TOTAL DUE         $ 42.93
Thank you for your visit!
"""

ocr_service = ReceiptOCRProcessor(simulated_ocr_text)
parsed_receipt = ocr_service.parse_receipt()
print("Simulated OCR Receipt Extraction Result:")
for k, v in parsed_receipt.items():
    print(f"  {k:<18}: {v}")

# =====================================================================
# 2. Integrating External C Libraries via ctypes
# =====================================================================
header("2. Calling Compiled C Libraries via ctypes")

try:
    if sys.platform == "win32":
        # Load C Runtime on Windows
        c_lib = ctypes.cdll.msvcrt
    else:
        # Load standard C library on POSIX
        c_lib = ctypes.CDLL("libc.so.6")

    # 1. Calling C puts function
    c_lib.puts.argtypes = [ctypes.c_char_p]
    c_lib.puts.restype = ctypes.c_int
    print("Executing C runtime function 'puts':")
    c_lib.puts(b"   [C Runtime] Message printed directly by compiled C library!")

    # 2. Calling C math functions if available
    c_lib.pow.argtypes = [ctypes.c_double, ctypes.c_double]
    c_lib.pow.restype = ctypes.c_double
    result_pow = c_lib.pow(ctypes.c_double(3.0), ctypes.c_double(4.0))
    print(f"C runtime calculation: 3.0 ^ 4.0 = {result_pow}")
except Exception as err:
    print(f"C Library ctypes demonstration note: {err}")

# =====================================================================
# 3. Advanced String Formatting with F-Strings
# =====================================================================
header("3. Advanced F-String Formatting Specifiers")

currency = 9845210.7589
percentage = 0.87654
binary_mask = 42

print(f"Currency Comma & Precision : ${currency:,.2f}")
print(f"Percentage Format          : {percentage:.1%}")
print(f"Padded Hexadecimal         : 0x{binary_mask:04X}")
print(f"Binary Representation      : {binary_mask:08b}")

# Self-documenting debug expressions (Python 3.8+)
cpu_cores = 8
memory_gb = 32
print(f"Debug Specifier Output: {cpu_cores=}, {memory_gb=}")

# =====================================================================
# 4. Web Scraping Essentials
# =====================================================================
header("4. Web Scraping & HTML Parsing")

class SimpleProductScraper(HTMLParser):
    """Extracts product titles and prices from HTML markup."""
    def __init__(self):
        super().__init__()
        self.in_product_title = False
        self.in_product_price = False
        self.products = []
        self._current_title = ""

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        css_class = attr_dict.get("class", "")
        if "product-title" in css_class:
            self.in_product_title = True
        elif "product-price" in css_class:
            self.in_product_price = True

    def handle_endtag(self, tag):
        self.in_product_title = False
        self.in_product_price = False

    def handle_data(self, data):
        data = data.strip()
        if not data:
            return
        if self.in_product_title:
            self._current_title = data
        elif self.in_product_price:
            self.products.append({"title": self._current_title, "price": data})

sample_html = """
<div class="catalog">
    <div class="item">
        <h2 class="product-title">Python FastTrack Workbook</h2>
        <span class="product-price">$49.99</span>
    </div>
    <div class="item">
        <h2 class="product-title">Mastering Microservices Guide</h2>
        <span class="product-price">$79.99</span>
    </div>
</div>
"""

scraper = SimpleProductScraper()
scraper.feed(sample_html)
print("Scraped Products from HTML:")
for prod in scraper.products:
    print(f"  {prod['title']} -> {prod['price']}")

# =====================================================================
# 5. Robust Error Handling & Custom Exceptions
# =====================================================================
header("5. Error Handling Architecture & Custom Exceptions")

class PaymentGatewayError(Exception):
    """Base exception for payment infrastructure."""
    pass

class InsufficientBalanceException(PaymentGatewayError):
    def __init__(self, balance: float, required: float):
        self.balance = balance
        self.required = required
        super().__init__(f"Transaction declined: Required ${required:.2f}, but only ${balance:.2f} available.")

def process_debit(balance: float, charge_amount: float) -> float:
    if charge_amount <= 0:
        raise ValueError("Charge amount must be positive.")
    if charge_amount > balance:
        raise InsufficientBalanceException(balance, charge_amount)
    return balance - charge_amount

# Exception Handling Cycle
for attempt in [50.0, 500.0, -10.0]:
    try:
        current_bal = 100.0
        print(f"\nAttempting charge of ${attempt:.2f} against balance ${current_bal:.2f}...")
        new_bal = process_debit(current_bal, attempt)
    except InsufficientBalanceException as ibe:
        print(f"   [HANDLED BUSINESS ERROR]: {ibe}")
    except ValueError as ve:
        print(f"   [HANDLED VALIDATION ERROR]: {ve}")
    else:
        print(f"   [SUCCESS]: Charge approved! Remaining balance: ${new_bal:.2f}")
    finally:
        print("   [AUDIT]: Transaction ledger update concluded.")

if __name__ == "__main__":
    print("\n[SUCCESS] Module 9 Teaching Code executed successfully!")

