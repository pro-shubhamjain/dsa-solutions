const { factorial, factorialRecur } = require('./factorial');

test('factorial of 0 and 1 is 1', () => {
  expect(factorial(0)).toEqual(1);
  expect(factorial(1)).toEqual(1);
});

test('factorial of 5 is 120', () => {
  expect(factorial(5)).toEqual(120);
});

test('factorial rejects negative numbers', () => {
  expect(factorial(-3)).toEqual('Factorial is not defined for negative numbers');
});

test('factorialRecur matches iterative factorial', () => {
  expect(factorialRecur(5)).toEqual(120);
  expect(factorialRecur(0)).toEqual(1);
});
