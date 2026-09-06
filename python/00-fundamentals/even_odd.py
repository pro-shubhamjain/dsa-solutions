"""
Problem: Even or Odd
Pattern: Fundamentals (modulo, list generation)
Time: O(1) for check_even_odd, O(n) for print_even_odd | Space: O(1) / O(n)

check_even_odd: classify a single positive number as even or odd.
print_even_odd: label every number from 1 to n as even or odd.

Input:  check_even_odd(4)
Output: 'Even number'

Input:  print_even_odd(2)
Output: ['1: Odd Number', '2: Even Number']
"""

def check_even_odd(input_num):
    if input_num <= 0:
        return 'Not valid number'
    return 'Even number' if input_num % 2 == 0 else 'Odd number'


def print_even_odd(input_num):
    if input_num <= 0:
        return 'Not valid number'
    return [
        f"{i + 1}: {'Even Number' if (i + 1) % 2 == 0 else 'Odd Number'}"
        for i in range(input_num)
    ]


if __name__ == "__main__":
    print(check_even_odd(4))       # Even number
    print(print_even_odd(2))       # ['1: Odd Number', '2: Even Number']
