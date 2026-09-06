"""
Problem: Reverse String and Integer
Pattern: Two Pointers (string/number reversal)
Time: O(n) | Space: O(n)

reverse_string: reverse the characters of a string.
reverse_integer: reverse the digits of an integer, preserving its sign.

Input:  reverse_string('abcd')
Output: 'dcba'

Input:  reverse_integer(-2359)
Output: -9532
"""

def reverse_string(s):
    return s[::-1] if s else s


def reverse_integer(input_num):
    sign = -1 if input_num < 0 else 1
    reversed_digits = str(abs(int(input_num)))[::-1]
    return int(reversed_digits) * sign


if __name__ == "__main__":
    print(reverse_string('abcd'))       # dcba
    print(reverse_integer(-2359))       # -9532
