"""
Problem: Max Char
Pattern: Arrays & Hashing (frequency counting)
Time: O(n) | Space: O(n)

Given a string, return the character used most often in it.

Input:  max_char('abcccccccd')
Output: 'c'
"""
import re
from collections import Counter

def max_char(input_str):
    cleaned = re.sub(r'[^\w]', '', input_str)
    counts = Counter(cleaned)
    return max(counts, key=counts.get) if counts else ''


# Alternative: sort characters, then count runs of equal adjacent chars in
# one pass. Time: O(n log n) instead of O(n), but avoids building an
# explicit frequency map -- worth mentioning as a trade-off.
def max_char_sorted(input_str):
    chars = sorted(re.sub(r'[^\w]', '', input_str))
    max_char_val, max_count = '', 0
    current_char, current_count = '', 0
    for c in chars:
        if c == current_char:
            current_count += 1
        else:
            current_char, current_count = c, 1
        if current_count > max_count:
            max_count, max_char_val = current_count, current_char
    return max_char_val


if __name__ == "__main__":
    print(max_char('abcccccccd'))  # c
