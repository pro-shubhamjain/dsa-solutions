"""
Problem: Array Chunk
Pattern: Arrays & Hashing (list slicing)
Time: O(n) | Space: O(n)

Given a list and a chunk size, split it into sublists of that length
(the last chunk may be shorter).

Input:  chunk([1, 2, 3, 4, 5], 2)
Output: [[1, 2], [3, 4], [5]]
"""

def chunk(array, size):
    result = []
    index = 0
    while index < len(array):
        result.append(array[index:index + size])
        index += size
    return result


# Alternative: build with a list comprehension over range steps instead of
# a while-loop + slicing. Same O(n) time, more Pythonic one-liner.
def chunk_comprehension(array, size):
    return [array[i:i + size] for i in range(0, len(array), size)]


if __name__ == "__main__":
    print(chunk([1, 2, 3, 4, 5], 2))  # [[1, 2], [3, 4], [5]]
