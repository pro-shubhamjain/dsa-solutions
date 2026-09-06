"""
Problem: Merge Intervals
Pattern: Intervals (sort + sweep)
Time: O(n log n) | Space: O(n)

Given a list of [start, end] intervals, merge all overlapping ones.

Input:  [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
"""

def merge_intervals(intervals):
    if len(intervals) == 0:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0][:]]

    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(current[1], previous[1])
        else:
            merged.append(current[:])

    return merged


# Alternative: recursive merge instead of an iterative loop.
# Same O(n log n) time (dominated by the sort), different control flow.
def merge_intervals_recursive(intervals):
    if len(intervals) == 0:
        return []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    def merge_from(index, acc):
        if index == len(sorted_intervals):
            return acc
        current = sorted_intervals[index]
        if acc and current[0] <= acc[-1][1]:
            acc[-1][1] = max(acc[-1][1], current[1])
        else:
            acc.append(current[:])
        return merge_from(index + 1, acc)

    return merge_from(0, [])


if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # [[1, 6], [8, 10], [15, 18]]
