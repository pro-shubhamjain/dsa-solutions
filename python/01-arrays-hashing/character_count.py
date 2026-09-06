"""
Problem: Character Count / Run-Length Encoding
Pattern: Arrays & Hashing (string traversal)
Time: O(n) | Space: O(n)

count_char_serialize: run-length-encode a string -- each run of repeated
characters becomes "<char><count>".
count_all_char: count total occurrences of every character in a string.

Input:  count_char_serialize("abbbccddddaab")
Output: "a1b3c2d4a2b1"

Input:  count_all_char("aabbbc")
Output: {'a': 2, 'b': 3, 'c': 1}
"""
import re
from collections import Counter

def count_char_serialize(s):
    count = 1
    result = ''
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1
    return result


def count_all_char(s):
    cleaned = re.sub(r'[^a-z0-9]', '', s, flags=re.IGNORECASE)
    return dict(Counter(cleaned))


if __name__ == "__main__":
    print(count_char_serialize("abbbccddddaab"))  # a1b3c2d4a2b1
    print(count_all_char("aabbbc"))                # {'a': 2, 'b': 3, 'c': 1}
