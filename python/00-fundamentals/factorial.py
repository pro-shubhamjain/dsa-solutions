"""
Problem: Factorial
Pattern: Fundamentals (recursion vs iteration)
Time: O(n) | Space: O(1) iterative, O(n) recursive (call stack)

Compute n! = n * (n-1) * ... * 1, with 0! = 1! = 1.

Input:  factorial(5)
Output: 120
"""
from functools import reduce

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return reduce(lambda a, b: a * b, range(1, n + 1), 1)


def factorial_recur(n):
    if n == 0:
        return 1
    return n * factorial_recur(n - 1)


if __name__ == "__main__":
    print(factorial(5))        # 120
    print(factorial_recur(5))  # 120
