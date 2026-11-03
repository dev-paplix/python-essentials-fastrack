"""
=============================================================================
Course   : Python Essentials [FastTrack] - Day 1
Module   : Module 3 - Numeric in Python
Audience : Absolute Beginners
Topic    : Student Hands-On Practice Exercises
=============================================================================

RULES FOR MODULE 3 EXERCISES:
- Only use variables, arithmetic operators, and the math module.
- NO functions (def) required.
- NO if / else statements required.
- NO loops (for / while) required.
=============================================================================
"""

import math

print("=" * 70)
print("MODULE 3: HANDS-ON PRACTICE EXERCISES FOR STUDENTS")
print("=" * 70)

# ===========================================================================
# EXERCISE 1: MODULO ARITHMETIC - CLOCK TIME CALCULATOR
# ===========================================================================
# Goal: Calculate the time on a 24-hour clock after N hours have passed.
#
# Scenario:
# Current hour is 21:00 (9 PM).
# A flight delay adds 7 hours.
# What time will it be on the 24-hour clock?
# Formula: (current_hour + added_hours) % 24
# ===========================================================================
print("\n--- EXERCISE 1: 24-HOUR CLOCK CALCULATOR ---")

current_hour = 21
flight_delay_hours = 7

# Calculate new hour using modulo
arrival_hour = (current_hour + flight_delay_hours) % 24

print("Current Hour :", current_hour, ":00")
print("Delay        :", flight_delay_hours, "hours")
print("Arrival Hour :", arrival_hour, ":00")


# ===========================================================================
# EXERCISE 2: PACKAGING DISTRIBUTION (FLOOR DIVISION & MODULO)
# ===========================================================================
# Goal: Use // and % to package products into shipping cartons.
#
# Scenario:
# A factory produces 254 smartphones.
# Each shipping box holds 15 phones.
# Calculate:
# 1. How many complete boxes can be shipped?
# 2. How many leftover phones remain in the warehouse?
# ===========================================================================
print("\n--- EXERCISE 2: PACKAGING DISTRIBUTION ---")

total_phones = 254
box_capacity = 15

full_boxes = total_phones // box_capacity
leftover_phones = total_phones % box_capacity

print("Total Phones Produced :", total_phones)
print("Full Shipping Boxes   :", full_boxes)
print("Leftover Phones       :", leftover_phones)


# ===========================================================================
# EXERCISE 3: GEOMETRY WIZARD (CIRCLE & SPHERE FORMULAS)
# ===========================================================================
# Goal: Use math.pi and exponentiation (**) to calculate circle & sphere metrics.
#
# Given:
# radius = 6.0
# Formulas:
# - Circle Area   = pi * radius^2
# - Sphere Volume = (4/3) * pi * radius^3
# ===========================================================================
print("\n--- EXERCISE 3: GEOMETRY WIZARD ---")

radius = 6.0

circle_area = math.pi * (radius ** 2)
sphere_volume = (4 / 3) * math.pi * (radius ** 3)

print("Radius         :", radius)
print("Circle Area    :", round(circle_area, 2))
print("Sphere Volume  :", round(sphere_volume, 2))


# ===========================================================================
# EXERCISE 4: VEHICLE FUEL EFFICIENCY CALCULATOR
# ===========================================================================
# Goal: Calculate fuel economy and trip travel expenses.
#
# Scenario:
# Distance from KL to Penang = 350 km.
# Fuel efficiency of car = 7.5 liters per 100 km.
# Fuel price = RM 2.05 per liter.
#
# Formula:
# liters_needed = (distance / 100) * fuel_efficiency
# total_cost = liters_needed * fuel_price
# ===========================================================================
print("\n--- EXERCISE 4: TRIP FUEL EXPENSE ---")

distance_km = 350.0
liters_per_100km = 7.5
price_per_liter = 2.05

liters_needed = (distance_km / 100.0) * liters_per_100km
total_fuel_cost = liters_needed * price_per_liter

print("Travel Distance :", distance_km, "km")
print("Total Fuel Used :", round(liters_needed, 2), "liters")
print("Total Fuel Cost : RM", round(total_fuel_cost, 2))


# ===========================================================================
# EXERCISE 5: SHIPPING WAREHOUSE CONTAINER ESTIMATION
# ===========================================================================
# Goal: Use math.ceil() to determine total cargo trucks needed.
#
# Scenario:
# A shipment has 142 pallets.
# Each transport truck can carry at most 25 pallets.
# Even if a truck is only partially filled, a full truck must be booked.
# Use math.ceil() to find how many trucks to book!
# ===========================================================================
print("\n--- EXERCISE 5: TRUCK FLEET BOOKING ---")

total_pallets = 142
truck_capacity = 25

trucks_needed = math.ceil(total_pallets / truck_capacity)

print("Total Pallets to Move :", total_pallets)
print("Truck Max Capacity    :", truck_capacity)
print("Total Trucks to Book  :", trucks_needed)

print("\n" + "=" * 70)
print("[SUCCESS] All Module 3 Practice Exercises Completed Successfully!")
print("=" * 70)
