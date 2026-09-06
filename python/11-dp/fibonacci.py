"""
Problem: Fibonacci
Pattern: Dynamic Programming (memoization)
Time: fibonacci_cache O(n) / naive fibonacci O(2^n) | Space: O(n) / O(n) call stack

Return the n-th entry in the Fibonacci sequence:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Input:  fibonacci_cache(10)
Output: 55
"""

def fibonacci(n):
    """Naive recursion -- O(2^n), kept to show the improvement memoization gives."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_cache(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fibonacci_cache(n - 1, memo) + fibonacci_cache(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(fibonacci(4))          # 3
    print(fibonacci_cache(10))   # 55
