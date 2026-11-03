"""
Module 10: OS Utilities and File Handling - Teaching Code
Instructor Demonstration Script
Course: Python Essentials FastTrack
"""

import os
import sys
from pathlib import Path
import csv
import json
import tempfile

def header(title: str):
    print("\n" + "=" * 60)
    print(f" {title.upper()} ")
    print("=" * 60)

# =====================================================================
# 1. Modern Filesystem Pathing with pathlib.Path
# =====================================================================
header("1. Modern Filesystem Pathing with pathlib")

current_dir = Path.cwd()
print(f"Current Working Directory : {current_dir}")
print(f"Home Directory            : {Path.home()}")

# Dynamic path resolution using `/` operator
mock_target = current_dir / "logs" / "archive" / "server_2026.log"
print(f"Path Object               : {mock_target}")
print(f"File Name (.name)         : {mock_target.name}")
print(f"File Stem (.stem)         : {mock_target.stem}")
print(f"File Suffix (.suffix)     : {mock_target.suffix}")
print(f"Parent Directory (.parent): {mock_target.parent}")

# Environment variables
user_env = os.environ.get("USERNAME") or os.environ.get("USER") or "DefaultUser"
print(f"Current OS User           : {user_env}")

# =====================================================================
# 2. File I/O Mechanics: Context Managers & Encodings
# =====================================================================
header("2. File Reading & Writing with Context Managers")

# Create a temporary directory for demonstrations
temp_dir = Path(tempfile.gettempdir()) / "python_fasttrack_demo"
temp_dir.mkdir(parents=True, exist_ok=True)
sample_text_path = temp_dir / "system_status.txt"

# Writing and Appending
with open(sample_text_path, mode="w", encoding="utf-8") as file:
    file.write("[2026-11-03 09:00:00] Server process started\n")
    file.write("[2026-11-03 09:05:00] Initialized 4 database worker threads\n")

with open(sample_text_path, mode="a", encoding="utf-8") as file:
    file.write("[2026-11-03 09:10:00] Healthcheck 200 OK\n")

print(f"Wrote log file to: {sample_text_path}")
print(f"File size in bytes: {sample_text_path.stat().st_size}")

# Reading line-by-line
print("\nReading contents line-by-line:")
with open(sample_text_path, mode="r", encoding="utf-8") as file:
    for line_no, line in enumerate(file, start=1):
        print(f"  Line {line_no}: {line.strip()}")

# =====================================================================
# 3. Structured Data: CSV & JSON Manipulation
# =====================================================================
header("3. Structured Processing: CSV (DictReader/Writer) & JSON")

csv_file_path = temp_dir / "employees.csv"
records = [
    {"EmpID": "1001", "Name": "Alice Walker", "Department": "Data Science", "Salary": "95000"},
    {"EmpID": "1002", "Name": "Robert Chen", "Department": "DevOps", "Salary": "105000"},
    {"EmpID": "1003", "Name": "Farah Aziz", "Department": "Cybersecurity", "Salary": "112000"},
]

# Write CSV with DictWriter
fields = ["EmpID", "Name", "Department", "Salary"]
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)

print(f"Exported CSV records to: {csv_file_path}")

# Read CSV with DictReader and compute department totals
dept_salaries = {}
with open(csv_file_path, mode="r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        dept = row["Department"]
        sal = float(row["Salary"])
        dept_salaries[dept] = sal

print("Parsed CSV into Department Salary Mapping:")
for dept, sal in dept_salaries.items():
    print(f"  {dept:<15}: ${sal:,.2f}")

# JSON Export and Import
json_file_path = temp_dir / "config.json"
app_config = {
    "version": "3.11.2",
    "cluster": "southeast-asia-1",
    "auto_scale": True,
    "metrics": dept_salaries
}

with open(json_file_path, mode="w", encoding="utf-8") as jf:
    json.dump(app_config, jf, indent=4)

with open(json_file_path, mode="r", encoding="utf-8") as jf:
    loaded_config = json.load(jf)
print(f"\nLoaded JSON configuration successfully (Cluster: {loaded_config['cluster']})")

if __name__ == "__main__":
    print("\n[SUCCESS] Module 10 Teaching Code executed successfully!")

