"""
Problem: FizzBuzz
Pattern: Fundamentals (conditionals, modulo)
Time: O(n) | Space: O(n) for the list version, O(1) for the print version

For each number 1..n: print/collect "fizz" if divisible by 3, "buzz" if
divisible by 5, "fizzbuzz" if divisible by both, otherwise the number itself.

Input:  fizz_buzz_list(5)
Output: [1, 2, 'fizz', 4, 'buzz']
"""

def fizz_buzz_list(input_num):
    if input_num < 1:
        return input_num
    result = []
    for i in range(1, input_num + 1):
        fizz = i % 3 == 0
        buzz = i % 5 == 0
        result.append('fizzbuzz' if fizz and buzz else 'fizz' if fizz else 'buzz' if buzz else i)
    return result


# Alternative: prints each value instead of returning a list.
def fizz_buzz_print(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


if __name__ == "__main__":
    print(fizz_buzz_list(15))
