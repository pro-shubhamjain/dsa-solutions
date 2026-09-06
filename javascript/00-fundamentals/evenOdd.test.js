const { checkEvenOdd, printEvenOdd } = require('./evenOdd');

test('checkEvenOdd identifies even numbers', () => {
  expect(checkEvenOdd(4)).toEqual('Even number');
});

test('checkEvenOdd identifies odd numbers', () => {
  expect(checkEvenOdd(7)).toEqual('Odd number');
});

test('checkEvenOdd rejects non-positive input', () => {
  expect(checkEvenOdd(0)).toEqual('Not valid number');
  expect(checkEvenOdd(-2)).toEqual('Not valid number');
});

test('printEvenOdd returns a labeled list up to n', () => {
  const result = printEvenOdd(2);
  expect(result).toEqual(['1: Odd Number', '2: Even Number']);
});
