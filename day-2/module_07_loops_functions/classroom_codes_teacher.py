import copy

def header(title):
    print("\n"+ "="*70)
    print(f"{title.upper()}")
    print("="*70)

header("Loop Fundamentals")

# Print range
print("range(5) until:", end="")
for i in range(5): # range(5) means 0, 1, 2, 3, 4
    print(i, end=" ")
print()

print("range(10, 25, 5) until:", end="")
for i in range(10, 26, 5):
    print(i, end=" ")
print()

print("range(5, 0, -1) until:", end="")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Iterating Strings and Lists
print("\n Iterating over characther and strings:")
for i in "PYTHON":
    print(f"[{i}]", end=" ")
print()

# While loop
print("\n while loop in rocket lunching")
countdown = 10
while countdown > 0:
    print(f"The missile is lunching in {countdown}.....")
    countdown -=1
print("Liftoff!!!!!!!!!")

# Simulating the network connection

print("\n Network connectivity search")
attempt = 1
max_retries = 10
connected = False

while attempt <= max_retries and not connected:
    print(f" Attempts: {attempt} of {max_retries} connecting to the network.....")
    if attempt == 5:
        connected = True
        print("Connection established susccessfully")
    else:
        print("Connection failed")
    attempt +=1

# Loop control: break, continue, and pass

print("\n loop control")
print("Priting odd numbers from 1 to 9 using continue:")

for n in range(1, 10):
    if n % 2 == 0:
        continue
    print(n, end=" ")
print()

# for-else and while-else
def finding_failing_record(records: list, treshold: int = 60):
    for rec in records:
        if rec["score"] < treshold:
            print(f" [FOUND] failing student: {rec['name']} ({rec['score']})")
            break
    else:
        print(f" [PASS] All {len(records)} students met or exceed {treshold}!")

good_records = [{"name": "Amar", "score": 85},{"name": "Fikri","score": 92}]
bad_records = [{"name": "Alicent", "score": 75}, {"name":"Henry", "score": 40}]

print("\n Searching for good records:")
finding_failing_record(good_records)
print("\n Searching for bad records:")
finding_failing_record(bad_records)

# Iteration utilizing with enumerate() and zip()
print("\n enumerate() and zip()")
students = ["Syafiq", "Victor", "Jane", "Joana"]
scores = [92, 88, 75, 90]
attendance = [98.0, 76.5, 85.2, 100.0]

for rank, (student, score, att) in enumerate(zip(students, scores, attendance), start=1):
    print(f"The ranking is {rank}: {student:<20} Score={score}, Attendance={att}%")

header("The Ternary Condition Operator")

print("\n Tempreture classification:")
tempretures = [18.5, 20.2, 22.0, 28.0, 31, 35]

for temp in tempretures:
    label = "Warm" if temp >= 25.0 else "Cool"
    print(f"{temp:4.1f} C -> {label}")

print("\nClamping values between 0 and 100:")
raw_inputes = [-15, 45, 120, 88, -5, 100]
for val in raw_inputes:
    clamped = 0 if val < 0 else( 100 if val> 100 else val)
    print(f"Raw: {val:>4} -< Clamped: {clamped:>3}") 

# Ternary transformation and filtering
print("\nTernary iside List Comprehension (Transformation Vs Filtering):")
numbers = [-5, 12, 0, -3, 8, 1]

# replacing negatives with 0
recrified = [x if x >0 else 0 for x in numbers]
# Filtering: keep only positives
positives = [x for x in numbers if x>0]
print(f"\nOriginal numbers: {numbers}")
print(f"\nRectified numbers: {recrified}")
print(f"\nPositive only numbers: {positives}")

header("Working with arrays")

# 1D arrays (list)
daily_sales = [1100.0, 1550.0, 420.0, 340.0, 1750.0]

total_sale = 0.0
highest_sale = daily_sales[0]

for sale in daily_sales:
    total_sale +=sale 
    if sale > highest_sale:
        highest_sale = sale

avg_sale = total_sale / len(daily_sales)
print(f"Daily Sales: {daily_sales}")
print(f"Total Sale: RM{total_sale:.2f} | Average Sale: RM{avg_sale:.2f} | Peak: RM{highest_sale:.2f}")

# Index-based
adjusted_sales = daily_sales.copy()
for i in range(len(adjusted_sales)):
    # Apply 10% bonus
    adjusted_sales[i] = round(adjusted_sales[i]* 1.10 if adjusted_sales[1] > avg_sale else adjusted_sales[1], 2)
print(f"Adjusted Sales (with bonus): {adjusted_sales}")

# 2D Arrays or Matrix

matrix_2d = [
    [22, 25, 28, 23],
    [19, 21, 20, 22],
    [31, 33, 29, 30]
]

print("2D Grid display")
for r_idx, row in enumerate(matrix_2d):
    row_str = " ".join(f"{val:>2} C" for val in row)
    print(f" Zone {r_idx}: [ {row_str} ]")

num_rows = len(matrix_2d)
num_cols = len(matrix_2d[0])
print(f"\nThe number of rows: {num_rows}")
print(f"\nThe number of columns: {num_cols}")

# Breaking down the matrix
print("\nRow Sums:")
for r in range(num_rows):
    row_sum = 0
    for c in range(num_cols):
        row_sum +=matrix_2d[r][c]
    print(f" Zone {r} Total: {row_sum}")

print("\nColumn Sums:")
for c in range(num_cols):
    col_sum = 0
    for r in range(num_rows):
        col_sum +=matrix_2d[r][c]
    print(f" Time Slot {c} Total: {col_sum}")

# Extracting diagonal in matrix
square_matrix = [
    [10, 2, 3],
    [4, 20, 6],
    [7, 8, 30]
]
diagonal = [square_matrix[i][i] for i in range(len(square_matrix))]
print(f"\nSquare Matrix Primary Diagonal: {diagonal}")

""" Ternary operation for tempreture clasification

matrix_2d = [
    [22, 25, 28, 23],
    [19, 21, 20, 22],
    [31, 33, 29, 30]
]
"""
classified_grid = []
for row in matrix_2d:
    clasified_row = ["Hot" if cell >= 25 else "Comfort" for cell in row]
    classified_grid.append(clasified_row)

print("\nClassified 2D grid:")
for row in classified_grid:
    print(row)

# 3D Arrays (Cubes/Tensors)

building_tempretures = [
    # floor 0
    [
        [20.5, 21.0], # room 0 first number demostrates the sensor 0 and second demonstrates sensor 1
        [22.0, 22.5], # room 1
        [19.8, 20.2]  # room 2
    ],
    # floor 1 
    [
        [24.0, 24.5], # room 0
        [28.5, 29.0], # room 1
        [23.0, 23.5]  # room 2
    ]
]

total_building_sum = 0
total_sensor_count = 0
hotspot_treshhold = 26.0
hotspots = []

for floor_idx, floor in enumerate(building_tempretures):
    floor_sum = 0.0
    floor_count = 0
    for room_idx , room in enumerate(floor):
        for sensor_idx , temp in enumerate(room):
            floor_sum += temp
            floor_count += 1
            total_building_sum +=temp
            total_sensor_count += 1

            # Check for hotspots
            if temp > hotspot_treshhold:
                hotspots.append((floor_idx, room_idx, sensor_idx, temp))
    
    floor_avg = floor_sum/ floor_count
    print(f"\nFloor {floor_idx}: Average Temp = {floor_avg:.2f} C (Sensors: {floor_count})")

building_avg = total_building_sum / total_sensor_count
print(f"\nBuiding-wide Average Temp: {building_avg:.2f} C")
print(f"\nHotspots detected (>{hotspot_treshhold} C)")

for f, r, s, t in hotspots:
    print(f"\n -> Floor {f}, Room {r}, Sensor {s}: {t} C")

# Alert system if it hits the treshhold of 26 C

status_cube = []
for floor in building_tempretures:
    floor_status = []
    for room in floor:
        room_status = ["Alert" if sensor > hotspot_treshhold else "Normal" for sensor in room]
        floor_status.append(room_status)
    status_cube.append(floor_status)

print(f"\n3D status cube (floor 1, room 1 ): {status_cube[1][1]}")
