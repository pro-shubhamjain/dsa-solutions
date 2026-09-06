const isPrime = require('./primeNumber');

test('isPrime is a function', () => {
  expect(typeof isPrime).toEqual('function');
});

test('correctly identifies prime numbers', () => {
  expect(isPrime(2)).toBe(true);
  expect(isPrime(3)).toBe(true);
  expect(isPrime(17)).toBe(true);
});

test('correctly identifies non-prime numbers', () => {
  expect(isPrime(1)).toBe(false);
  expect(isPrime(4)).toBe(false);
  expect(isPrime(15)).toBe(false);
});

test('numbers <= 1 are never prime', () => {
  expect(isPrime(0)).toBe(false);
  expect(isPrime(-5)).toBe(false);
});
