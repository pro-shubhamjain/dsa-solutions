const { fizzBuzzArray, fizzBuzz1 } = require('./fizzbuzz');

beforeEach(() => {
  jest.spyOn(console, 'log').mockImplementation(() => {});
});

afterEach(() => {
  console.log.mockRestore();
});

describe('fizzBuzzArray', () => {
  test('fizzBuzzArray is a function', () => {
    expect(typeof fizzBuzzArray).toEqual('function');
  });

  test('returns correctly spelled fizz/buzz/fizzbuzz -- regression test for the typo bug', () => {
    // Previously returned 'fiz' and 'fizbuzz' (missing a 'z') due to a typo.
    expect(fizzBuzzArray(5)).toEqual([1, 2, 'fizz', 4, 'buzz']);
  });

  test('returns fizzbuzz for multiples of both 3 and 5', () => {
    expect(fizzBuzzArray(15)[14]).toEqual('fizzbuzz');
  });
});

describe('fizzBuzz1', () => {
  test('fizzBuzz function is defined', () => {
    expect(fizzBuzz1).toBeDefined();
  });

  test('Calling fizzbuzz with `5` prints out 5 statements', () => {
    fizzBuzz1(5);

    expect(console.log.mock.calls.length).toEqual(5);
  });

  test('Calling fizzbuzz with 15 prints out the correct values', () => {
    fizzBuzz1(15);

    expect(console.log.mock.calls[0][0]).toEqual(1);
    expect(console.log.mock.calls[1][0]).toEqual(2);
    expect(console.log.mock.calls[2][0]).toEqual('fizz');
    expect(console.log.mock.calls[3][0]).toEqual(4);
    expect(console.log.mock.calls[4][0]).toEqual('buzz');
    expect(console.log.mock.calls[5][0]).toEqual('fizz');
    expect(console.log.mock.calls[6][0]).toEqual(7);
    expect(console.log.mock.calls[7][0]).toEqual(8);
    expect(console.log.mock.calls[8][0]).toEqual('fizz');
    expect(console.log.mock.calls[9][0]).toEqual('buzz');
    expect(console.log.mock.calls[10][0]).toEqual(11);
    expect(console.log.mock.calls[11][0]).toEqual('fizz');
    expect(console.log.mock.calls[12][0]).toEqual(13);
    expect(console.log.mock.calls[13][0]).toEqual(14);
    expect(console.log.mock.calls[14][0]).toEqual('fizzbuzz');
  });
});
