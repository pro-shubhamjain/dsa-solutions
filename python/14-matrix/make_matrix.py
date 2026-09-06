"""
Problem: Spiral Matrix
Pattern: Matrix traversal (boundary shrinking)
Time: O(n^2) | Space: O(n^2)

Write a function that accepts an integer N and returns an NxN spiral matrix.

Input:  matrix(3)
Output: [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
"""

def matrix(n):
    results = [[None] * n for _ in range(n)]

    counter = 1
    start_row, end_row = 0, n - 1
    start_col, end_col = 0, n - 1

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            results[start_row][col] = counter
            counter += 1
        start_row += 1

        for row in range(start_row, end_row + 1):
            results[row][end_col] = counter
            counter += 1
        end_col -= 1

        for col in range(end_col, start_col - 1, -1):
            results[end_row][col] = counter
            counter += 1
        end_row -= 1

        for row in range(end_row, start_row - 1, -1):
            results[row][start_col] = counter
            counter += 1
        start_col += 1

    return results


# Alternative: direction-vector simulation (walk right/down/left/up, turning
# when the next cell would leave bounds or has already been filled) instead
# of tracking four shrinking boundaries. Same O(n^2) time -- generalizes
# better to non-square m x n spirals.
def matrix_direction_vector(n):
    results = [[None] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    dir_index = 0
    row, col = 0, 0

    for counter in range(1, n * n + 1):
        results[row][col] = counter
        dr, dc = directions[dir_index]
        next_row, next_col = row + dr, col + dc

        out_of_bounds = not (0 <= next_row < n and 0 <= next_col < n)
        already_filled = not out_of_bounds and results[next_row][next_col] is not None

        if out_of_bounds or already_filled:
            dir_index = (dir_index + 1) % 4

        row += directions[dir_index][0]
        col += directions[dir_index][1]

    return results


if __name__ == "__main__":
    print(matrix(3))
    # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
