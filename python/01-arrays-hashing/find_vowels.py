"""
Problem: Count Vowels
Pattern: Arrays & Hashing (string scanning)
Time: O(n) | Space: O(1)

Count how many vowels (a, e, i, o, u -- case-insensitive) appear in a string.

Input:  count_vowels('aeiou')
Output: 5
"""

def count_vowels_type1(s):
    vowels = set('aeiou')
    return sum(1 for c in s.lower() if c in vowels)


def count_vowels(s):
    return count_vowels_type1(s)  # same approach; Python has no regex-match-count
                                    # shortcut cleaner than the set-based scan


if __name__ == "__main__":
    print(count_vowels('aeiou'))  # 5
