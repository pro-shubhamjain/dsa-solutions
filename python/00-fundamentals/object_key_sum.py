"""
Problem: Object Key Sum
Pattern: Fundamentals (dict/list manipulation)
Time: O(n) | Space: O(k) where k = number of distinct keys

Given a list of single-key dicts, sum the values grouped by key.

Input:  [{'a': 2}, {'a': 2}, {'b': 1}, {'b': 9}]
Output: {'a': 4, 'b': 10}
"""

def obj_key_sum(arr):
    output = {}
    for obj in arr:
        key = next(iter(obj))  # assumes each dict has only one key
        output[key] = output.get(key, 0) + obj[key]
    return output


# Alternative: same idea using collections.defaultdict instead of .get().
# Same O(n) time.
from collections import defaultdict

def obj_key_sum_defaultdict(arr):
    output = defaultdict(int)
    for obj in arr:
        key = next(iter(obj))
        output[key] += obj[key]
    return dict(output)


if __name__ == "__main__":
    print(obj_key_sum([{'a': 2}, {'a': 2}, {'b': 1}, {'b': 9}]))  # {'a': 4, 'b': 10}
