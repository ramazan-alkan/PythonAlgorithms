import time # Import time for sleep

# Fibonacci

def Fibonacci(a,b,sleep):
    while True: # While forever
        print(a) # Print result
        c = a + b # Get sum a + b
        a = b # a equal to b
        b = c # b equal to c
        time.sleep(sleep) # Wait for a while

# Test

Fibonacci(0,1,.2) # 0 is a value / 1 is b value / .2 is speed