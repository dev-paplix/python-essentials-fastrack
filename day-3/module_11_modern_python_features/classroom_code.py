import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def header(title):
    print("\n" + "=" * 70)
    print(f"{title.upper()}")
    print("=" * 70)

# match-case pattern matching

header("match-case pattern matching")

def process_cli_command(command: list):
    match command:
        case['quit'] | ["exit"]:
            return "Action: Terminating application"
        
        case["get", str(key)]:
            return f"Action:  Fetching key '{key}' from the store."
        
        case["set", str(key), value]:
            return f"Action:  Setting key '{key}' to the value {value}"

        case["delete", str(key)] if key.startswith("system_"):
            return f"Action Blocked! deleting system {key} requires root priviledge"
        
        case["delete", str(key)]:
            return f"Action: Deleted key {key}"
        
        case["batch", *operations]:
            return f"Action: Executing batch of {len(operations)} sub-commands: {operations}"

        case _:
            return f"Action: invalid command {command}"

cli_tests = [
    ["get", "user_01"],
    ["set", "cache_ttl", 3600],
    ["delete", "system_kernel"],
    ["delete", "temp"],
    ["batch", "sync", "flush", "compact"],
    ["exit"],
    ["unkown", 1, 2, 3, 4]
]

for cmd in cli_tests:
    print(f"Input: {cmd!s:<35} -> {process_cli_command(cmd)}")


# match-case for dictionaries and mapping

header("Match-Case for dictionaries and mapping")

def handle_events(payload: dict)-> str:
    match payload:
        
        case {"event": "payment_successful", "amount": amt, "currency": cur}:
            return f"Processed reciept for {amt:,.2f} {cur}"

        case {"event": "payment_failed", "reason": reason}:
            return f"Failed becuase: {reason}"

        case {"event": "user_signup", "user": {"email": email, "type": "customer"}}:
            return f"Welcome to our shop user: {email}"

        case {"event": "user_signup", "user": {"email": email}}:
            return f"Welcome to our demo: {email}"

        case _:
            return "Unauthorized access"

events = [
    {"event": "payment_successful", "amount": 310.50, "currency": "RM"},
    {"event": "payment_failed", "reason": "Insufficient fund"},
    {"event": "user_signup", "user": {"email": "arman@gmail.com", "type": "customer"}},
    {"event": "user_signup", "user": {"email": "arman@yahoo.com"}}
]

for ev in events:
    print(f"Output -> {handle_events(ev)}")


# F-String Modern Python

# I/O Parallazation with ThreadPoolExecutor
header("I/O Parallazation with ThreadPoolExecutor")

def simulate_io_download(task_id: int, duration_sec: float) -> str:
    time.sleep(duration_sec)
    return f"Task- {task_id} downloaded in {duration_sec:.1f}s"

download_tasks = [(1, 5.3), (2, 12.1), (3, 6.5), (4, 9.3), (5, 8.2)]

start_time = time.time()
print(f"Beginning cocurrent excution of {len(download_tasks)} download operations ....")

# Lets excecute over 5 workers threads
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(simulate_io_download, tid, dur) for tid, dur in download_tasks]
    for completed in as_completed(futures):
        print(f" [Done]: {completed.result()}")

elapsed = time.time() - start_time
print(f"\nTotal elapsed parallel execution time: {elapsed:.2f} seconds")
print(f"( A run would require {sum(d for _, d in download_tasks):.2f} seconds)")
