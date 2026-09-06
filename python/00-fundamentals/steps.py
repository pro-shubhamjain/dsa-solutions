"""
Problem: Steps / Staircase Patterns
Pattern: Fundamentals (nested loops, string building)
Time: O(n^2) | Space: O(n) per printed row

Print an n-row staircase of '#' characters, in various orientations.

Input:  steps(3)
Output (printed):
  #
  ##
  ###
"""

def steps(n):
    for row in range(n):
        stair = ''
        for column in range(n):
            stair += '#' if column <= row else ' '
        print(stair)


def steps_rtl(input_num):
    """Right-to-left staircase -- '#' block flush against the right edge."""
    for row in range(input_num - 1, -1, -1):
        level = ''
        for col in range(input_num):
            level += '#' if col >= row else ' '
        print(level)


def steps_ltr(input_num):
    """Ascending staircase, left-aligned: row 0 has 1 '#', row (n-1) has n."""
    for row in range(input_num):
        print('#' * (row + 1))


def down_to_top(input_num):
    """Descending staircase, left-aligned -- mirror image of steps_ltr."""
    for row in range(input_num):
        print('#' * (input_num - row))


if __name__ == "__main__":
    steps(3)
