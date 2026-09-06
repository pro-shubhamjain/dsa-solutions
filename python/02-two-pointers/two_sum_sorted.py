"""
Problem: Two Sum II - Input Array Is Sorted
Pattern: Two Pointers
Time: O(n) | Space: O(1)

Input:  nums = [1, 2, 4, 6, 8, 9], target = 11
Output: [1, 5]  (nums[1] + nums[5] = 2 + 9 = 11)
"""

def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []


# Alternative: hash map lookup instead of two pointers. Same O(n) time and
# O(n) space instead of O(1) -- but does NOT require the array to be sorted,
# so it's the more general approach (classic "Two Sum I" solution).
def two_sum_hash_map(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([1, 2, 4, 6, 8, 9], 11))  # [1, 5]
    print(two_sum_hash_map([4, 1, 9, 6, 2, 8], 11))  # [2, 4]
