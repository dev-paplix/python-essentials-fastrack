"""
Module 10: OS Utilities and File Handling - Student Practice Exercises
Course: Python Essentials FastTrack

Instructions:
1. Complete the challenges below using pathlib, csv, and json.
2. Run this script to test your solutions against the automated assertions.
"""

from pathlib import Path
import csv
import json
import tempfile
import shutil

# =====================================================================
# Exercise 1: Log File Error Extractor
# =====================================================================
# Problem Statement:
# Write a function `extract_error_logs(log_file_path: Path) -> list`
# Given the path to a log text file, read through each line and extract
# only lines that contain the keyword "ERROR" or "CRITICAL" (case-insensitive).
# Return a list of the trimmed matching lines.

def extract_error_logs(log_file_path: Path) -> list:
    """Reads a log file and returns all error and critical severity lines."""
    matches = []
    with open(log_file_path, mode="r", encoding="utf-8") as f:
        for line in f:
            upper = line.upper()
            if "ERROR" in upper or "CRITICAL" in upper:
                matches.append(line.strip())
    return matches


# =====================================================================
# Exercise 2: CSV Salary Aggregator & Exporter
# =====================================================================
# Problem Statement:
# Write `generate_department_summary(input_csv: Path, output_json: Path) -> dict`
# Input CSV format:
#   Name,Department,Salary
# Compute the total salary payout and employee count for each department:
# {
#   "IT": {"total_salary": 200000.0, "headcount": 2},
#   ...
# }
# Save this dictionary to `output_json` formatted with indent=2, and also return the dict.

def generate_department_summary(input_csv: Path, output_json: Path) -> dict:
    """Aggregates salary data per department from CSV and exports to JSON."""
    summary = {}
    with open(input_csv, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row["Department"]
            salary = float(row["Salary"])
            if dept not in summary:
                summary[dept] = {"total_salary": 0.0, "headcount": 0}
            summary[dept]["total_salary"] += salary
            summary[dept]["headcount"] += 1
            
    # Round totals
    for dept in summary:
        summary[dept]["total_salary"] = round(summary[dept]["total_salary"], 2)
        
    with open(output_json, mode="w", encoding="utf-8") as jf:
        json.dump(summary, jf, indent=2)
        
    return summary


# =====================================================================
# Exercise 3: Automated File Organizer Simulation
# =====================================================================
# Problem Statement:
# Write a function `organize_directory_by_extension(source_dir: Path) -> dict`
# Scans all files directly inside `source_dir`:
# - For each file (skip directories), inspect its extension (e.g. '.pdf', '.jpg', '.txt').
# - Create a subdirectory named after the extension without the dot (e.g. 'pdf', 'jpg', 'txt').
#   If a file has no extension, place it into a folder named 'other'.
# - Move the file into its respective folder.
# - Return a dict summarizing count of files moved per extension: {'pdf': 2, 'jpg': 1, ...}

def organize_directory_by_extension(source_dir: Path) -> dict:
    """Organizes files into subfolders based on extension."""
    counts = {}
    for item in list(source_dir.iterdir()):
        if item.is_file():
            ext = item.suffix.lstrip(".").lower()
            folder_name = ext if ext else "other"
            target_subfolder = source_dir / folder_name
            target_subfolder.mkdir(exist_ok=True)
            
            # Relocate file
            destination = target_subfolder / item.name
            shutil.move(str(item), str(destination))
            
            counts[folder_name] = counts.get(folder_name, 0) + 1
            
    return counts


# =====================================================================
# Verification Test Suite
# =====================================================================
def run_tests():
    print("=" * 60)
    print("RUNNING MODULE 10 PRACTICE TESTS")
    print("=" * 60)

    test_env = Path(tempfile.gettempdir()) / "mod10_tests"
    if test_env.exists():
        shutil.rmtree(test_env)
    test_env.mkdir(parents=True)

    # Test Exercise 1
    log_file = test_env / "app.log"
    log_file.write_text(
        "INFO: Started\nERROR: DB Timeout\nDEBUG: Ping\nCRITICAL: Out of memory\n",
        encoding="utf-8"
    )
    errors = extract_error_logs(log_file)
    assert len(errors) == 2
    assert "ERROR: DB Timeout" in errors
    assert "CRITICAL: Out of memory" in errors
    print("  [PASS] Exercise 1: Log Error Extractor works correctly!")

    # Test Exercise 2
    csv_file = test_env / "staff.csv"
    csv_file.write_text(
        "Name,Department,Salary\nAlice,IT,80000\nBob,HR,60000\nCharlie,IT,90000\n",
        encoding="utf-8"
    )
    json_out = test_env / "summary.json"
    summary = generate_department_summary(csv_file, json_out)
    assert summary["IT"]["headcount"] == 2
    assert summary["IT"]["total_salary"] == 170000.0
    assert summary["HR"]["headcount"] == 1
    assert json_out.exists()
    print("  [PASS] Exercise 2: CSV Department Aggregator works correctly!")

    # Test Exercise 3
    inbox = test_env / "inbox"
    inbox.mkdir()
    (inbox / "doc1.pdf").touch()
    (inbox / "doc2.pdf").touch()
    (inbox / "photo.jpg").touch()
    (inbox / "notes.txt").touch()
    (inbox / "no_ext").touch()

    org_summary = organize_directory_by_extension(inbox)
    assert org_summary == {"pdf": 2, "jpg": 1, "txt": 1, "other": 1}
    assert (inbox / "pdf" / "doc1.pdf").exists()
    assert (inbox / "jpg" / "photo.jpg").exists()
    print("  [PASS] Exercise 3: Automated File Organizer works correctly!")

    # Clean up test temp files
    shutil.rmtree(test_env)
    print("\nAll Module 10 exercises passed successfully! Outstanding work!\n")

if __name__ == "__main__":
    run_tests()

