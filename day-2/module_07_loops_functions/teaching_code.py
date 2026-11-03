"""
Module 7: Loops and Functions - Teaching Code
Instructor Demonstration Script
Course: Python Essentials FastTrack
"""

def header(title: str):
    print("\n" + "=" * 60)
    print(f" {title.upper()} ")
    print("=" * 60)

# =====================================================================
# 1. Advanced Loop Constructs: enumerate, zip, and loop-else
# =====================================================================
header("1. Iteration Patterns: enumerate, zip, and loop-else")

students = ["Alice", "Bob", "Charlie", "Diana"]
scores = [92, 85, 78, 96]
attendance = [98.0, 91.5, 85.0, 100.0]

print("Looping with zip and enumerate:")
for rank, (name, score, att) in enumerate(zip(students, scores, attendance), start=1):
    print(f"Rank {rank}: {name:<8} Score={score} Attendance={att}%")

# Sentinel search demonstrating for-else
def find_first_failing_student(student_records: list, threshold: int = 60):
    for rec in student_records:
        if rec["score"] < threshold:
            print(f"   Found student below threshold: {rec['name']} ({rec['score']})")
            break
    else:
        print(f"   All {len(student_records)} students met or exceeded the threshold of {threshold}!")

records_good = [{"name": "A", "score": 85}, {"name": "B", "score": 92}]
records_bad = [{"name": "A", "score": 85}, {"name": "C", "score": 45}]

print("\nSearching records_good:")
find_first_failing_student(records_good)

print("\nSearching records_bad:")
find_first_failing_student(records_bad)

# =====================================================================
# 2. Variable Scope & The LEGB Rule
# =====================================================================
header("2. Variable Scope Demonstration (LEGB)")

app_environment = "PRODUCTION"  # Global

def outer_service():
    service_id = "SVC-AUTH-01"   # Enclosing
    
    def inner_worker():
        request_id = "REQ-999"   # Local
        print(f"   [inner_worker] Local: {request_id}, Enclosing: {service_id}, Global: {app_environment}")
        
    inner_worker()

outer_service()

# =====================================================================
# 3. Variadic Arguments (*args, **kwargs) & Keyword-Only Arguments
# =====================================================================
header("3. Advanced Parameter Packing & Unpacking")

def build_api_endpoint(base_url: str, *path_segments, version: str = "v1", **query_params) -> str:
    """
    Constructs a RESTful URL string dynamically.
    - base_url : Positional argument
    - *path_segments : Packed tuple of path components
    - version : Keyword argument with default
    - **query_params : Packed dictionary of URL query params
    """
    clean_base = base_url.rstrip("/")
    clean_paths = "/".join(segment.strip("/") for segment in path_segments)
    url = f"{clean_base}/{version}/{clean_paths}"
    
    if query_params:
        query_string = "&".join(f"{k}={v}" for k, v in query_params.items())
        url += f"?{query_string}"
        
    return url

generated_url = build_api_endpoint(
    "https://api.gemrain.net",
    "courses",
    "python-fasttrack",
    "modules",
    version="v2",
    limit=10,
    sort="asc"
)
print(f"Constructed REST URL:\n{generated_url}")

# =====================================================================
# 4. List, Dict, and Set Comprehensions
# =====================================================================
header("4. Modern Comprehensions")

raw_salaries = [45000, 60000, 85000, 120000, 150000]

# List Comprehension with condition
high_earner_bonuses = [int(s * 0.15) for s in raw_salaries if s >= 80000]
print(f"High Earner Bonuses: {high_earner_bonuses}")

# Dictionary Comprehension
exchange_rate_usd_to_myr = 4.45
salaries_myr = {f"EMP_{idx+1}": round(usd * exchange_rate_usd_to_myr, 2) for idx, usd in enumerate(raw_salaries)}
print(f"Salaries Converted to MYR:\n{salaries_myr}")

if __name__ == "__main__":
    print("\n[SUCCESS] Module 7 Teaching Code executed successfully!")

