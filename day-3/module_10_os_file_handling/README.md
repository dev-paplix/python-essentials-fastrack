# Module 10: Operating System Utilities and File Handling

---

## 1. Utilizing OS Utilities in Python

Python provides two main modules for interacting with the operating system:
1. **`os` & `sys`**: Low-level platform utilities, environment variables, command-line arguments.
2. **`pathlib.Path` (Python 3.4+)**: The modern, object-oriented industry standard for filesystem path operations.

### Cross-Platform Path Manipulation with `pathlib`
Never concatenate file paths with strings like `"C:\\folder\\" + filename` or Linux slashes `"folder/" + filename`. Use `pathlib.Path` with the `/` division operator:

```python
from pathlib import Path

# Working directory and base paths
base_dir = Path.cwd()
data_file = base_dir / "data" / "users.json"

# Useful Path attributes and methods:
data_file.name          # 'users.json' (filename with extension)
data_file.stem          # 'users' (filename without extension)
data_file.suffix        # '.json' (file extension)
data_file.parent        # Path object representing parent directory
data_file.exists()      # True / False
data_file.is_file()     # True / False
data_file.is_dir()      # True / False
data_file.stat().st_size # File size in bytes
```

### Directory Scans and Globbing
```python
# Create directories safely (including parents):
reports_dir = Path("exports/daily_reports")
reports_dir.mkdir(parents=True, exist_ok=True)

# Find all CSV files in a directory recursively:
for csv_path in Path(".").rglob("*.csv"):
    print(f"Discovered CSV: {csv_path}")
```

### Environment Variables
```python
import os

# Retrieve environment variable with default fallback:
api_key = os.environ.get("DATABASE_URL", "sqlite:///default.db")
```

---

## 2. File Reading and Writing Techniques

### The Context Manager Pattern (`with open`)
Always open files using the `with` statement. The context manager guarantees that system file descriptors are immediately closed, even if unexpected errors or exceptions occur:

```python
# Reading line-by-line (Memory Efficient for large files)
with open("system.log", "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())

# Writing and Appending
with open("audit.txt", "w", encoding="utf-8") as f:
    f.write("Line 1: System initialized\n")

with open("audit.txt", "a", encoding="utf-8") as f:
    f.write("Line 2: User logged in\n")
```

---

## 3. Structured File Reading Methods: CSV and JSON

### Working with CSV Files (`csv.DictReader` & `csv.DictWriter`)
The `csv` module provides dictionary-based access to tabular records:

```python
import csv

# Reading CSV as dictionaries
with open("employees.csv", mode="r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Department"], row["Salary"])

# Writing CSV from dictionaries
fields = ["Name", "Department", "Salary"]
data = [
    {"Name": "Alice", "Department": "Engineering", "Salary": 95000},
    {"Name": "Bob", "Department": "Sales", "Salary": 82000}
]

with open("output.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
```

### Working with JSON Files (`json.load` & `json.dump`)
- `json.load(f)` reads JSON directly from a file stream into Python data structures.
- `json.dump(obj, f, indent=4)` serializes Python data directly into a file stream.

---

## 4. Practical Project: Automated File Organizer
A ubiquitous DevOps automation task:
- Scan an unsorted target directory (e.g. `Downloads/`).
- Inspect file extensions (`.pdf`, `.jpg`, `.csv`, `.py`).
- Create corresponding destination subfolders automatically.
- Safely relocate files into their respective categorical folders.

