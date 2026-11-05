"""
Module 7: Loops and Functions - Teaching Code
Instructor Demonstration Script
Course: Python Essentials FastTrack

Topics Covered:
1. Core Loop Fundamentals: 'for' and 'while' Loops
2. The Ternary Conditional Operator (Conditional Expressions)
3. Looping with Arrays: 1D, 2D (Matrices), and 3D (Cubes / Tensors)
4. Variable Scope & The LEGB Rule
5. Variadic Arguments (*args, **kwargs) & Keyword-Only Parameters
6. Modern Comprehensions (List, Dict, Set, and Nested Comprehensions)
"""

def header(title: str):
    print("\n" + "=" * 65)
    print(f" {title.upper()} ")
    print("=" * 65)


# =====================================================================
# 1. Core Loop Fundamentals: 'for' and 'while' Loops
# =====================================================================
header("1. Core Loop Fundamentals: for and while Loops")

# --- 1A. The for Loop & range() Variations ---
print("--- 1A: for loop with range() variants ---")
print("range(5) ->", end=" ")
for i in range(5):
    print(i, end=" ")
print()

print("range(10, 25, 5) ->", end=" ")
for i in range(10, 25, 5):
    print(i, end=" ")
print()

print("range(5, 0, -1) [Countdown] ->", end=" ")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Iterating across sequences (strings, lists)
print("\nIterating over characters of a string:")
for ch in "PYTHON":
    print(f"[{ch}]", end=" ")
print()

# --- 1B. The while Loop: Counter, Condition, and Retry Mechanics ---
print("\n--- 1B: while loop mechanics ---")
countdown = 3
while countdown > 0:
    print(f"  Rocket launching in {countdown}...")
    countdown -= 1
print("  Liftoff!")

# While loop with simulated retry logic
print("\nSimulating network retry with while loop:")
attempt = 1
max_retries = 3
connected = False

while attempt <= max_retries and not connected:
    print(f"  Attempt {attempt} of {max_retries} connecting to database...")
    if attempt == 2:  # simulate success on 2nd attempt
        connected = True
        print("  Connection established successfully!")
    attempt += 1

# --- 1C. Loop Control: break, continue, pass, and loop-else ---
print("\n--- 1C: Loop Control (break, continue, else) ---")
print("Printing odd numbers from 1 to 9 using continue:")
for n in range(1, 10):
    if n % 2 == 0:
        continue  # skip even numbers
    print(n, end=" ")
print()

# Sentinel search demonstrating for-else and while-else
def find_failing_record(records: list, threshold: int = 60):
    """Loop-else executes ONLY if loop finishes without hitting break."""
    for rec in records:
        if rec["score"] < threshold:
            print(f"   [FOUND] Failing student: {rec['name']} ({rec['score']})")
            break
    else:
        print(f"   [PASS] All {len(records)} students met or exceeded {threshold}!")

records_good = [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}]
records_bad = [{"name": "Charlie", "score": 88}, {"name": "Diana", "score": 45}]

print("\nSearching records_good:")
find_failing_record(records_good)
print("Searching records_bad:")
find_failing_record(records_bad)

# --- 1D. Iteration Utilities: enumerate() and zip() ---
print("\n--- 1D: enumerate() and zip() ---")
students = ["Alice", "Bob", "Charlie", "Diana"]
scores = [92, 85, 78, 96]
attendance = [98.0, 91.5, 85.0, 100.0]

for rank, (name, score, att) in enumerate(zip(students, scores, attendance), start=1):
    print(f"  Rank {rank}: {name:<8} Score={score} Attendance={att}%")


# =====================================================================
# 2. The Ternary Conditional Operator
# =====================================================================
header("2. The Ternary Conditional Operator")

# Syntax: <value_if_true> if <condition> else <value_if_false>
score = 78
status = "PASS" if score >= 60 else "FAIL"
print(f"Score {score} -> Result: {status}")

# Ternary inside a loop for inline classification
print("\nClassifying batch temperatures using ternary operator:")
temperatures = [18.5, 22.0, 31.5, 15.0, 28.5]
for temp in temperatures:
    label = "WARM" if temp >= 25.0 else "COOL"
    print(f"  {temp:4.1f} C -> {label}")

# Ternary clamping (bounding a value between bounds)
print("\nClamping values between 0 and 100:")
raw_inputs = [-15, 45, 120, 88, -5, 100]
for val in raw_inputs:
    clamped = 0 if val < 0 else (100 if val > 100 else val)
    print(f"  Raw: {val:>4} -> Clamped: {clamped:>3}")

# Ternary transformation vs filtering in List Comprehensions
print("\nTernary inside List Comprehension (Transformation vs Filtering):")
numbers = [-5, 12, 0, -3, 8, -1]
# Transformation: replaces negative numbers with 0, retains positives
rectified = [x if x > 0 else 0 for x in numbers]
# Filtering: keeps ONLY positive numbers
positives_only = [x for x in numbers if x > 0]
print(f"  Original       : {numbers}")
print(f"  Rectified (x if x>0 else 0) : {rectified}")
print(f"  Filtered  ([x for x if x>0]): {positives_only}")


# =====================================================================
# 3. Looping with Arrays (1D, 2D, and 3D Arrays)
# =====================================================================
header("3. Looping with Arrays: 1D, 2D, and 3D Arrays")

# ---------------------------------------------------------------------
# 3A. 1D Arrays (Lists): Traversal, In-Place Mutation, and Accumulators
# ---------------------------------------------------------------------
print("--- 3A: 1D Array Operations ---")
daily_sales = [1200.0, 1550.0, 980.0, 2100.0, 1750.0]

# Direct value traversal (Accumulator pattern)
total_sales = 0.0
highest_sale = daily_sales[0]
for sale in daily_sales:
    total_sales += sale
    if sale > highest_sale:
        highest_sale = sale
avg_sales = total_sales / len(daily_sales)
print(f"Daily Sales: {daily_sales}")
print(f"Total: ${total_sales:.2f} | Average: ${avg_sales:.2f} | Peak: ${highest_sale:.2f}")

# Index-based traversal for in-place modification (applying 10% bonus)
adjusted_sales = daily_sales.copy()
for i in range(len(adjusted_sales)):
    # Apply 10% bonus if day exceeded average, else keep flat (ternary!)
    adjusted_sales[i] = round(adjusted_sales[i] * 1.10 if adjusted_sales[i] > avg_sales else adjusted_sales[i], 2)
print(f"Adjusted Sales (with bonus): {adjusted_sales}")

# ---------------------------------------------------------------------
# 3B. 2D Arrays (Grids / Matrices - Nested Loops)
# ---------------------------------------------------------------------
print("\n--- 3B: 2D Array (Matrix / Grid) Nested Loops ---")
# 3x4 Matrix representing sensor readings across 3 zones and 4 time slots
matrix_2d = [
    [22, 25, 28, 23],  # Zone 0
    [19, 21, 20, 22],  # Zone 1
    [31, 33, 29, 30]   # Zone 2
]

# Traversing and pretty-printing the 2D grid
print("2D Grid Display (Zone x Time):")
for r_idx, row in enumerate(matrix_2d):
    row_str = "  ".join(f"{val:>2} C" for val in row)
    print(f"  Zone {r_idx}: [ {row_str} ]")

# Row totals and Column totals
num_rows = len(matrix_2d)
num_cols = len(matrix_2d[0])

print("\nRow Sums:")
for r in range(num_rows):
    row_sum = 0
    for c in range(num_cols):
        row_sum += matrix_2d[r][c]
    print(f"  Zone {r} Total: {row_sum}")

print("\nColumn Sums (Time slot totals across all zones):")
for c in range(num_cols):
    col_sum = 0
    for r in range(num_rows):
        col_sum += matrix_2d[r][c]
    print(f"  Time Slot {c} Total: {col_sum}")

# Extracting the primary diagonal of a square matrix
square_matrix = [
    [10,  2,  3],
    [ 4, 20,  6],
    [ 7,  8, 30]
]
diagonal = [square_matrix[i][i] for i in range(len(square_matrix))]
print(f"\nSquare Matrix Primary Diagonal: {diagonal}")

# 2D Transformation using Ternary Operator (Threshold Masking)
# Flagging values >= 25 as 'HOT', else 'COMFORT'
classified_grid = []
for row in matrix_2d:
    classified_row = ["HOT" if cell >= 25 else "COMFORT" for cell in row]
    classified_grid.append(classified_row)

print("Classified 2D Grid:")
for row in classified_grid:
    print(f"  {row}")

# ---------------------------------------------------------------------
# 3C. 3D Arrays (Cubes / Tensors - 3-Level Nested Loops)
# ---------------------------------------------------------------------
print("\n--- 3C: 3D Array (Cube / Tensor) 3-Level Nested Loops ---")
# Analogy: Multi-Floor Office Building
# building[floor][room][sensor]
# 2 Floors, 3 Rooms per floor, 2 Sensors per room
building_temps = [
    # Floor 0
    [
        [20.5, 21.0],  # Room 0 (Sensors A, B)
        [22.0, 22.5],  # Room 1
        [19.8, 20.2]   # Room 2
    ],
    # Floor 1
    [
        [24.0, 24.5],  # Room 0
        [28.5, 29.0],  # Room 1 (Hotspot room!)
        [23.0, 23.5]   # Room 2
    ]
]

# Traversing 3D volume with 3 nested loops
print("Traversing 3D Building Grid:")
total_building_sum = 0.0
total_sensor_count = 0
hotspot_threshold = 26.0
hotspots = []

for floor_idx, floor in enumerate(building_temps):
    floor_sum = 0.0
    floor_count = 0
    for room_idx, room in enumerate(floor):
        for sensor_idx, temp in enumerate(room):
            floor_sum += temp
            floor_count += 1
            total_building_sum += temp
            total_sensor_count += 1
            
            # Check for hotspot using ternary or conditional
            if temp > hotspot_threshold:
                hotspots.append((floor_idx, room_idx, sensor_idx, temp))
                
    floor_avg = floor_sum / floor_count
    print(f"  Floor {floor_idx}: Average Temp = {floor_avg:.2f} C (Sensors: {floor_count})")

building_avg = total_building_sum / total_sensor_count
print(f"\nBuilding-wide Average Temp: {building_avg:.2f} C")
print(f"Hotspots detected (> {hotspot_threshold} C):")
for f, r, s, t in hotspots:
    print(f"  -> Floor {f}, Room {r}, Sensor {s}: {t} C")

# 3D Transformation with Ternary Operator
# Replace reading with 'ALERT' if > threshold else 'NORMAL'
status_cube = []
for floor in building_temps:
    floor_status = []
    for room in floor:
        room_status = ["ALERT" if sensor > hotspot_threshold else "NORMAL" for sensor in room]
        floor_status.append(room_status)
    status_cube.append(floor_status)

print(f"\n3D Status Cube (Floor 1, Room 1): {status_cube[1][1]}")


# =====================================================================
# 4. Variable Scope & The LEGB Rule
# =====================================================================
header("4. Variable Scope Demonstration (LEGB)")

app_environment = "PRODUCTION"  # Global

def outer_service():
    service_id = "SVC-AUTH-01"   # Enclosing
    
    def inner_worker():
        request_id = "REQ-999"   # Local
        print(f"   [inner_worker] Local: {request_id}, Enclosing: {service_id}, Global: {app_environment}")
        
    inner_worker()

outer_service()


# =====================================================================
# 5. Variadic Arguments (*args, **kwargs) & Keyword-Only Arguments
# =====================================================================
header("5. Advanced Parameter Packing & Unpacking")

def build_api_endpoint(base_url: str, *path_segments, version: str = "v1", **query_params) -> str:
    """
    Constructs a RESTful URL string dynamically.
    - base_url       : Positional argument
    - *path_segments : Packed tuple of path components
    - version        : Keyword argument with default
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
# 6. List, Dict, Set, and Nested Comprehensions
# =====================================================================
header("6. Modern Comprehensions with Ternaries & 2D Nesting")

raw_salaries = [45000, 60000, 85000, 120000, 150000]

# List Comprehension with condition
high_earner_bonuses = [int(s * 0.15) for s in raw_salaries if s >= 80000]
print(f"High Earner Bonuses: {high_earner_bonuses}")

# List Comprehension with Ternary Transformation
bonus_tiers = [f"${int(s * 0.15)}" if s >= 80000 else f"${int(s * 0.05)}" for s in raw_salaries]
print(f"Tiered Bonuses (Ternary): {bonus_tiers}")

# Dictionary Comprehension
exchange_rate_usd_to_myr = 4.45
salaries_myr = {f"EMP_{idx+1}": round(usd * exchange_rate_usd_to_myr, 2) for idx, usd in enumerate(raw_salaries)}
print(f"Salaries Converted to MYR:\n{salaries_myr}")

# Nested (2D) List Comprehension: Flattening a 2D matrix
matrix_to_flatten = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_1d = [val for row in matrix_to_flatten for val in row]
print(f"Flattened 2D Matrix: {flattened_1d}")

# Generating a 2D Multiplication Table with nested comprehensions
multiplication_table = [[r * c for c in range(1, 6)] for r in range(1, 6)]
print("2D Multiplication Table (1-5):")
for r in multiplication_table:
    print(f"  {r}")

if __name__ == "__main__":
    print("\n[SUCCESS] Module 7 Teaching Code executed successfully!")
