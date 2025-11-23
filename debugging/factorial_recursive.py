#!/usr/bin/python3
import sys

# ------------------------------------------------------------
# Function: factorial
# Description:
#     Computes the factorial of a non-negative integer using
#     a recursive approach. The factorial of n (n!) is defined
#     as the product of all positive integers from 1 to n.
#     By definition, 0! = 1.
#
# Parameters:
#     n (int):
#         A non-negative integer whose factorial is to be calculated.
#         The function assumes valid input and does not handle
#         negative values or non-integer input.
#
# Returns:
#     int:
#         The factorial of the input value n.
#         Example:
#             factorial(0) -> 1
#             factorial(5) -> 120
# ------------------------------------------------------------
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

