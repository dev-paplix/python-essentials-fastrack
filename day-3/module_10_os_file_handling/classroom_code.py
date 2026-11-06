import os
import sys
import csv
import json
import tempfile
from pathlib import Path

def header(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70 + "\n")

# Working with pathlib
header("Working with pathlib")

current_dir = Path.cwd()
print(f"Current working directory: {current_dir}")
print(f"Home directory: {Path.home()}")

# Dynamic dir
sample_dir = current_dir / "logs" / "2026" / "python_logs_2026.log"
print(f"Path objects: {sample_dir}")
print(f"File Name: {sample_dir.name}")
print(f"File Stem: {sample_dir.stem}")
print(f"File Suffix: {sample_dir.suffix}")
print(f"Parent Directory: {sample_dir.parent}")

#Accessing enviromental variable
jwt_base = os.environ.get("JWT_TOKEN")
print(jwt_base)

# I/O Mechanics

header("Reading and writing with context manager")

#Create a temp directory
temp_dir = Path(tempfile.gettempdir()) / "python_code"
temp_dir.mkdir(parents=True, exist_ok=True)
sample_text_path = temp_dir / "system_status.txt"

# Wrting and appending
with open(sample_text_path, mode="w", encoding="utf-8") as file:
    file.write("[2026-11-06 14:20:00] The system is initiating\n")
    file.write("[2026-11-06 14:26:00] Everything is up and running\n")

with open(sample_text_path, mode="a", encoding="utf-8") as file:
    file.write("[2026-11-06 14:27:00] The system checked\n")

print(f"Wrote in the {sample_text_path}")
print(f"The stat and size are {sample_text_path.stat().st_size}")

# Reading line by line
print("\n Reading line by line:")

with open(sample_text_path, mode="r", encoding="utf-8") as file:
    for line_no, line in enumerate(file, start=1):
        print(f" Line{line_no}: {line.strip()}" )

# Wokring with CSV and JSON

header("CSV and JSON CRUD")

csv_file_path = temp_dir / "pricing.csv"

car_prices = [
    {"ID": "1001", "Product": "Toyota Corolla", "Year": "2021", "Price": "52000"},
    {"ID": "1002", "Product": "BMW X9", "Year": "2024", "Price": "144000"},
    {"ID": "1003", "Product": "Proton Saga", "Year": "2022", "Price": "18000"},
]

# Writing into CSV file
fields = ["ID", "Product", "Year", "Price"]

with open(csv_file_path, mode="w", encoding="utf-8", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(car_prices)

print(f"Exported Prices to the {csv_file_path}")

all_prices = {}
with open(csv_file_path, mode="r", encoding="utf-8", newline="") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        year = row["Year"]
        price = float(row["Price"])
        all_prices[year] = price

print("Maping the prices based on the manufacturing year\n")
for year, price in all_prices.items():
    print(f" {year:<20}: RM{price:,.2f}")

# JSON can be import and export as well
json_file_path = temp_dir / "crypto_pricing.json"

crypto_pricing = {
    "name": "BTC",
    "price": "$70,000",
    "currently_trading": True,
    "metrics": all_prices
}

with open(json_file_path, mode="w", encoding="utf-8") as jf:
    json.dump(crypto_pricing, jf, indent=4)


with open(json_file_path, mode="r", encoding="utf-8") as jf:
    loaded_prices = json.load(jf)

print(f"The json files is following:\n {loaded_prices['price']}, and is status:{loaded_prices['currently_trading']}")