# Factorial program student number:202510305
#  Factorial — Iterative Method
#  Computes n! using a loop
# 
def factorial_iterative(n):
    """Return n! computed iteratively."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1              # accumulator
    for i in range(1, n + 1):  # i goes 1..n
        result *= i         # result = result * i
    return result
# 
n = 7
answer = factorial_iterative(n)
print(f"Iterative:  {n}! = {answer}")
# 
#  Factorial — Recursive Method
#  Uses the relation  n! = n * (n-1)!
# 
def factorial_recursive(n):
    """Return n! computed recursively."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0 or n == 1:    # base case
        return 1
    return n * factorial_recursive(n - 1)  # recurse
# 
n = 7

answer = factorial_recursive(n)
print(f"Recursive:  {n}! = {answer}")
#  
for n in [0, 1, 5, 7, 10]:
    it = factorial_iterative(n)
    rc = factorial_recursive(n)
    match = "OK" if it == rc else "MISMATCH"
    print(f"n={n:>2}  iter={it:>8}  rec={rc:>8}  {match}")
n
