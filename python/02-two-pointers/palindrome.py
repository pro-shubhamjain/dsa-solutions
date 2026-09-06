"""
Problem: Palindrome
Pattern: Two Pointers (string comparison)
Time: O(n) | Space: O(n)

Check whether a string reads the same forwards and backwards.
Case-sensitive and whitespace-sensitive (no normalization applied).

Input:  palindrome('aba')
Output: True
"""

def palindrome(s):
    return s == s[::-1]


# Alternative: two-pointer comparison, no extra reversed string built.
# Same O(n) time, but O(1) space instead of O(n).
def palindrome_two_pointer(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(palindrome('aba'))  # True
