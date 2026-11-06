import sys
import ctypes
import re
from html.parser import HTMLParser

def header(title):
    print(f"\n" + "=" * 70)
    print(title)
    print("=" * 70)

# OCR
header("Optical Character Recognition (OCR) and Text Extraction")

class RecieptOcr:

    def __init__(self, raw_ocr_output: str):
        self.raw_ocr_output = raw_ocr_output

    def parse_recipt(self) -> dict:
        lines = [line.strip() for line in self.raw_ocr_output.strip().split("\n") if line.strip()]
        vendor = lines[0] if lines else "Unknown Vendor"

        # Finding the amount using regex to match currency patterns (including commas in numbers)
        # demonstration fetcher: RM, $ or any symbols and also 0.00 or 17.31 or 7,299.00
        amount_pattern = re.findall(r"RM\s*[\d,]+(?:\.\d{2})?", self.raw_ocr_output)
        amounts = [float(i.replace("RM", "").replace(",", "")) for i in amount_pattern]

        total = max(amounts) if amounts else 0.0

        return {
            "vendor": vendor,
            "total_extracted": total,
            "extracted_amounts": amounts
        }

sample_ocr_output = """
Electronics Store
Date: 2026-11-06
Iphone 18 x1                     RM 7,299.00
Samsung Galaxy S30 x1            RM 5,999.00
ACER Laptop x2                   RM 9,499.00
SST(10%)                         RM 2,279.80
Total:                           RM 25,077.80

All Amounts are inclusive of SST
No returns or exchanges after 7 days of purchase.
Thank you for shopping with us!

"""

ocr_processor = RecieptOcr(sample_ocr_output)
parsing_receipt = ocr_processor.parse_recipt()
print("Here is you OCR parsed receipt data:")

for key, value in parsing_receipt.items():
    print(f"{key:<20}: {value}")


# Integrate with C libraries in the machine
header("Integrating with C Libraries in Python")

try:
    if sys.platform == "win32": # Loading in C DLL for Windows
        c_lib = ctypes.cdll.msvcrt
    else: # Loading in C shared library for Linux and MacOS
        c_lib = ctypes.CDLL("libc.so.6")

    """CRUD = Create, Read, Update, Delete
    Python for: 
    Create = Post
    Update = Put
    Delete = Delete
    Read = Get
    """
    # Call for C input
    
    c_lib.puts.argtypes = [ctypes.c_char_p]
    c_lib.puts.restype = ctypes.c_int
    print("Excuting C function puts() from the C library:")
    c_lib.puts(b"Message is inside the C library, and it is printed using the C function puts()")

    # Call for C Math function
    c_lib.pow.argtypes = [ctypes.c_double, ctypes.c_double]
    c_lib.pow.restype = ctypes.c_double
    result_pow = c_lib.pow(ctypes.c_double(3.0), ctypes.c_double(4.0))
    print(f"Result of C function pow(3.0, 4.0): {result_pow}")
    a = 3.0
    b = 4.0
    print(f"\nusing basic math in python: {a ** b}")

except Exception as err:
    print(f"An error occurred: {err}")


# Advanced String formating with F-Strings
header("Advanced String Formatting with F-Strings")

currency = 874613.2323
percentage = 0.7541
binary_mask = 42

print(f"Currency with Comma & Precision: RM {(currency):,.2f}")
print(f"Percentage with Precision: {percentage:.2%}")
print(f"Padded Hexadecimal: 0x{binary_mask:04X}")
print(f"Binary Representation: {binary_mask:08b}")

# Self dbuging
cpu_cores = 8
memory_gb = 32
print(f"System Resources: CPU Cores: {cpu_cores=}, Memory: {memory_gb=}GB")

# Web Scraping and HTML Parsing
header("Web Scraping and HTML Parsing")

class WebScraper(HTMLParser):
    # Scraping to extract the product titles and prices

    def __init__(self):
        super().__init__()
        self.in_product_title = False
        self.in_product_price = False
        self.products = []
        self._current_title = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        css_class = attrs_dict.get("class", "")
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

sample_html_webpage = """
<html>
    <div class="all-products">
        <div class="product">
            <h2 class="product-title">Asus Gaming Laptop</h2>
            <p class="product-price">RM9899.99</p>
        </div>
        <div class="product">
            <h2 class="product-title">MSI Gaming Laptop</h2>
            <p class="product-price">RM8099.99</p>
        </div>
    </div>
</html>
"""

scrapper = WebScraper()
scrapper.feed(sample_html_webpage)
print("Extracted Products from HTML:")

for product in scrapper.products:
    print(f"Product Title: {product['title']}, Price: {product['price']}")


# Erro Handling and custom Exception
header("Error Handling and Custom Exceptions")


class PaymentGatewayError(Exception):
    pass

class InsufficientFundsError(PaymentGatewayError):
    def __init__(self, balance: float, required: float):
        self.balance = balance
        self.required = required
        super().__init__(f"Insufficient funds: Balance is {balance}, but {required} is required.")

def process_payment(balance: float, charge_amount: float) -> float:
    if charge_amount <= 0:
        raise ValueError("Charge amount must be positive.")
    if charge_amount > balance:
        raise InsufficientFundsError(balance, charge_amount)
    return balance - charge_amount

for attempt in [50.0, 500.0, -10.0]:
    try:
        current_balance = 100.0
        print(f"\n Attemting to charge of {attempt:.2f} from balance of {current_balance:.2f}")
        new_balance = process_payment(current_balance, attempt)

    except InsufficientFundsError as ibe:
        print(f"Payment failed: {ibe}")
    except ValueError as ve:
        print(f"Payment failed: {ve}")
    else:
        print(f"Payment successful! New balance: {new_balance:.2f}")
    finally:
        print("Payment processing attempt completed.")