"""
Problem 1: Currying
Pattern: Fundamentals (closures / functional programming)
Time: O(1) | Space: O(1)

Implement a curried calculator: calc() returns a chain of single-argument
functions -- add, sub, multi, divide -- ending in get_result() which
computes the final value.

Input:  calc()(10)(5)(20)(2)()   i.e. (10 - 5) * 20 / 2
Output: 50.0
"""

def calc():
    def add(i1):
        def sub(i2):
            def multi(i3):
                def divide(i4):
                    def get_result():
                        return ((i1 - i2) * i3) / i4
                    return get_result
                return divide
            return multi
        return sub
    return add


class FluentCalculator:
    """
    Alternative: fluent/chainable API instead of currying -- same idea
    (build a computation step by step) expressed as method chaining.

    Input:  FluentCalculator().add(5).sub(2).multiply(10).divided(2).get_result()
    Output: 15.0   i.e. ((0 + 5 - 2) * 10) / 2
    """
    def __init__(self):
        self.value = 0

    def add(self, num):
        self.value += num
        return self

    def sub(self, num):
        self.value -= num
        return self

    def multiply(self, num):
        self.value *= num
        return self

    def divided(self, num):
        if num != 0:
            self.value /= num
        else:
            print("Cannot divide by zero.")
        return self

    def get_result(self):
        return self.value


"""
Problem 2: Closures and loop variables (Python's version of the classic
JS `var`-in-a-loop gotcha)
Pattern: Fundamentals (closures / scoping)

In Python, a `for` loop variable is NOT scoped to the loop body -- it's a
regular variable in the enclosing scope, similar to JS `var`. A lambda that
closes over it directly captures the SAME variable, not its value at
creation time -- so by the time the lambdas run, the loop has finished and
the variable holds its final value.

Input:  closure_bug()
Output: 2, 2, 2   (all three print the final value of i, NOT 0, 1, 2)
"""
def closure_bug():
    fns = []
    for i in range(3):
        fns.append(lambda: print(i))
    for fn in fns:
        fn()


"""
Alternative fix: pass i as a default argument, which binds its value at
lambda-creation time instead of lookup time. This is the standard Python
idiom for this gotcha (there's no block-scoped `let` equivalent in Python).

Input:  closure_fixed()
Output: 0, 1, 2
"""
def closure_fixed():
    fns = []
    for i in range(3):
        fns.append(lambda i=i: print(i))
    for fn in fns:
        fn()


if __name__ == "__main__":
    print(calc()(10)(5)(20)(2)())  # 50.0
    print(FluentCalculator().add(5).sub(2).multiply(10).divided(2).get_result())  # 15.0
    closure_bug()     # 2, 2, 2
    closure_fixed()   # 0, 1, 2
