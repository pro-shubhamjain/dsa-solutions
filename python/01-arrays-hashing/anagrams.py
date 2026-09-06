"""
Problem: Anagrams
Pattern: Arrays & Hashing (string normalization)
Time: O(n log n) | Space: O(n)

Check whether two strings are anagrams of each other -- same characters,
same quantities, ignoring case, spaces, and punctuation.

Input:  anagrams('hello', 'llohe')
Output: True
"""
import re
from collections import Counter

def clean_string(s):
    return ''.join(sorted(re.sub(r'[^\w]', '', s).lower()))

def anagrams(string_a, string_b):
    return clean_string(string_a) == clean_string(string_b)


# Alternative: character-frequency comparison instead of sorting.
# Time: O(n) instead of O(n log n) -- genuinely better.
def anagrams_frequency_map(string_a, string_b):
    build = lambda s: Counter(re.sub(r'[^\w]', '', s).lower())
    return build(string_a) == build(string_b)


if __name__ == "__main__":
    print(anagrams('hello', 'llohe'))  # True
