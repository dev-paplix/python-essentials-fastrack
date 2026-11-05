def expensive_finder():
    print("Looking for expensive goods")
    return False

print("Test 1: False and expensive_finder()")
if False and expensive_finder():
    pass

print(" I was not expensive")

print("Test 2: True and expensive_finder()")
if True and expensive_finder():
    pass
print(" I was not expensive")