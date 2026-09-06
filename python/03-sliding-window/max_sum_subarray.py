"""
Problem: Maximum Sum Subarray of Size K
Pattern: Sliding Window (fixed size)
Time: O(n) | Space: O(1)

Input:  nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9  (subarray [5, 1, 3])
"""

def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


# Alternative: brute force -- recompute the sum of every window from scratch.
# Time: O(n*k) instead of O(n). Shows the naive first-attempt vs the
# optimized sliding-window version above.
def max_sum_subarray_brute_force(nums, k):
    max_sum = float('-inf')
    for i in range(len(nums) - k + 1):
        window_sum = sum(nums[i:i + k])
        max_sum = max(max_sum, window_sum)
    return max_sum


if __name__ == "__main__":
    print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9
    print(max_sum_subarray_brute_force([2, 1, 5, 1, 3, 2], 3))  # 9
