"""
Problem: Is Prime Number
Pattern: Fundamentals (trial division)
Time: O(sqrt(n)) | Space: O(1)

Check whether a number is prime by testing divisibility up to its square root.

Input:  is_prime(17)
Output: True
"""
import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# Alternative: 6k +/- 1 optimization -- after checking 2 and 3, every prime
# is of the form 6k+1 or 6k-1. Same O(sqrt(n)) complexity class, ~3x fewer
# iterations in practice.
def is_prime_optimized(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    print(is_prime(17))  # True
    print(is_prime(15))  # False
