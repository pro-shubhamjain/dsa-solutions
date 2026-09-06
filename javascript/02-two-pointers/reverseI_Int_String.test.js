const reverse = require('./reverseI_Int_String');

test('Reverse function exists', () => {
  expect(reverse.reverseInteger).toBeDefined();
  expect(reverse.reverseString).toBeDefined();
});

test('Reverse reverses a string', () => {
  expect(reverse.reverseString('abcd')).toEqual('dcba');
});

test('Reverse reverses a string', () => {
  expect(reverse.reverseString('  abcd')).toEqual('dcba  ');
});

test('reverseInteger handles 0 as an input', () => {
  expect(reverse.reverseInteger(0)).toEqual(0);
});

test('reverseInteger flips a positive number', () => {
  expect(reverse.reverseInteger(5)).toEqual(5);
  expect(reverse.reverseInteger(15)).toEqual(51);
  expect(reverse.reverseInteger(90)).toEqual(9);
  expect(reverse.reverseInteger(2359)).toEqual(9532);
});

test('reverseInteger flips a negative number', () => {
  expect(reverse.reverseInteger(-5)).toEqual(-5);
  expect(reverse.reverseInteger(-15)).toEqual(-51);
  expect(reverse.reverseInteger(-90)).toEqual(-9);
  expect(reverse.reverseInteger(-2359)).toEqual(-9532);
});
