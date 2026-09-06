"""
Problem: Pyramid
Pattern: Fundamentals (nested loops, string building)
Time: O(n^2) | Space: O(n) per printed row

Print a centered pyramid of '#' characters, n rows tall.

Input:  pyramid(3)
Output (printed):
    #
   ###
  #####
"""

def pyramid(input_num):
    cal_col = input_num * 2 - 1
    midpoint = cal_col // 2
    for row in range(input_num):
        level = ''
        for col in range(cal_col):
            if midpoint - row <= col <= midpoint + row:
                level += '#'
            else:
                level += ' '
        print(level)


# Alternative: build each row with str.center() instead of a
# character-by-character inner loop. Same O(n^2) total time, more concise.
def pyramid_center(input_num):
    width = input_num * 2 - 1
    for row in range(1, input_num + 1):
        hashes = '#' * (2 * row - 1)
        print(hashes.center(width))


if __name__ == "__main__":
    pyramid(3)
