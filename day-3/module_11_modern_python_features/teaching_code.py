"""
Module 11: Modern Python Features (3.10 & 3.11) - Teaching Code
Instructor Demonstration Script
Course: Python Essentials FastTrack
"""

import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def header(title: str):
    print("\n" + "=" * 60)
    print(f" {title.upper()} ")
    print("=" * 60)

# =====================================================================
# 1. Structural Pattern Matching: PEP 634 (Python 3.10+)
# =====================================================================
header("1. Structural Pattern Matching (match-case)")

def process_cli_command(command: list):
    """
    Demonstrates sequence unpacking, literal matching, and guards with match-case.
    """
    match command:
        case ["quit"] | ["exit"]:
            return "Action: Terminating application."
        
        case ["get", str(key)]:
            return f"Action: Fetching key '{key}' from store."
            
        case ["set", str(key), value]:
            return f"Action: Setting key '{key}' to value '{value}'."
            
        case ["delete", str(key)] if key.startswith("system_"):
            return f"Action: BLOCKED! Deleting system key '{key}' requires root privileges."
            
        case ["delete", str(key)]:
            return f"Action: Deleted key '{key}'."
            
        case ["batch", *operations]:
            return f"Action: Executing batch of {len(operations)} sub-commands: {operations}"
            
        case _:
            return f"Action: Invalid or unparseable command structure: {command}"

cli_tests = [
    ["get", "user_101"],
    ["set", "cache_ttl", 3600],
    ["delete", "system_kernel_param"],
    ["delete", "temp_session"],
    ["batch", "sync", "flush", "compact"],
    ["exit"],
    ["unknown", 1, 2, 3, 4]
]

for cmd in cli_tests:
    print(f"Input: {cmd!s:<35} -> {process_cli_command(cmd)}")

# =====================================================================
# 2. Structural Pattern Matching with Dictionaries (Mapping Patterns)
# =====================================================================
header("2. Mapping Patterns with Dictionaries")

def handle_webhook_event(payload: dict) -> str:
    match payload:
        case {"event": "payment_success", "amount": amt, "currency": cur}:
            return f"Processed receipt for {amt:,.2f} {cur}"
            
        case {"event": "payment_failed", "reason": reason}:
            return f"Triggered notification for failed transaction: {reason}"
            
        case {"event": "user_signup", "user": {"email": email, "tier": "premium"}}:
            return f"Welcomed VIP enterprise user: {email}"
            
        case {"event": "user_signup", "user": {"email": email}}:
            return f"Welcomed standard user: {email}"
            
        case _:
            return "Unhandled or unrecognized webhook event"

events = [
    {"event": "payment_success", "amount": 149.99, "currency": "USD"},
    {"event": "payment_failed", "reason": "Expired card token"},
    {"event": "user_signup", "user": {"email": "cto@enterprise.com", "tier": "premium"}},
    {"event": "user_signup", "user": {"email": "guest@gmail.com"}},
]

for ev in events:
    print(f"Webhook -> {handle_webhook_event(ev)}")

# =====================================================================
# 3. Modern F-String Customizations & Precision
# =====================================================================
header("3. Modern F-String Formatting Tricks")

voltage = 230.4567
current = 12.8942
power = voltage * current

# Self-documenting debug notation
print(f"Debug evaluation: {voltage=:.2f}V, {current=:.2f}A, {power=:.2f}W")

# Dynamic padding and alignment
headers = ["Sensor ID", "Status", "Reading"]
print(f"\n{headers[0]:<15} | {headers[1]:^10} | {headers[2]:>12}")
print("-" * 43)
sample_readings = [("SNS-001", "ACTIVE", 42.15), ("SNS-002", "STANDBY", 0.0), ("SNS-003", "ALERT", 99.88)]
for sid, stat, val in sample_readings:
    print(f"{sid:<15} | {stat:^10} | {val:>12.2f}")

# =====================================================================
# 4. I/O Parallelization with ThreadPoolExecutor
# =====================================================================
header("4. Parallel I/O using concurrent.futures.ThreadPoolExecutor")

def simulate_io_download(task_id: int, duration_sec: float) -> str:
    """Simulates an I/O network download that sleeps for duration_sec."""
    time.sleep(duration_sec)
    return f"Task-{task_id} downloaded in {duration_sec:.1f}s"

download_tasks = [(1, 0.3), (2, 0.4), (3, 0.2), (4, 0.3), (5, 0.2)]

start_time = time.time()
print(f"Beginning concurrent execution of {len(download_tasks)} download operations...")

# Execute downloads concurrently across 5 worker threads
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(simulate_io_download, tid, dur) for tid, dur in download_tasks]
    for completed_future in as_completed(futures):
        print(f"   [DONE]: {completed_future.result()}")

elapsed = time.time() - start_time
print(f"\nTotal elapsed parallel execution time: {elapsed:.2f} seconds")
print(f"(A sequential run would have required {sum(d for _, d in download_tasks):.2f} seconds!)")

if __name__ == "__main__":
    print("\n[SUCCESS] Module 11 Teaching Code executed successfully!")

