const { steps, stepsRTL, stepsLTR, downToTop } = require('./steps');

beforeEach(() => {
  jest.spyOn(console, 'log');
});

afterEach(() => {
  console.log.mockRestore();
});

describe('steps', () => {
  test('steps is a function', () => {
    expect(typeof steps).toEqual('function');
  });

  test('steps called with n = 1', () => {
    steps(1);
    expect(console.log.mock.calls[0][0]).toEqual('#');
    expect(console.log.mock.calls.length).toEqual(1);
  });

  test('steps called with n = 3', () => {
    steps(3);
    expect(console.log.mock.calls[0][0]).toEqual('#  ');
    expect(console.log.mock.calls[1][0]).toEqual('## ');
    expect(console.log.mock.calls[2][0]).toEqual('###');
    expect(console.log.mock.calls.length).toEqual(3);
  });
});

describe('stepsRTL', () => {
  test('stepsRTL called with n = 3', () => {
    stepsRTL(3);
    expect(console.log.mock.calls[0][0]).toEqual('  #');
    expect(console.log.mock.calls[1][0]).toEqual(' ##');
    expect(console.log.mock.calls[2][0]).toEqual('###');
    expect(console.log.mock.calls.length).toEqual(3);
  });
});

describe('stepsLTR', () => {
  test('stepsLTR called with n = 3 -- regression test for the off-by-one bug', () => {
    stepsLTR(3);
    // Previously produced ['', '#', '##'] due to the bug -- now correctly ascends from 1.
    expect(console.log.mock.calls[0][0]).toEqual('#');
    expect(console.log.mock.calls[1][0]).toEqual('##');
    expect(console.log.mock.calls[2][0]).toEqual('###');
    expect(console.log.mock.calls.length).toEqual(3);
  });
});

describe('downToTop', () => {
  test('downToTop called with n = 3', () => {
    downToTop(3);
    expect(console.log.mock.calls[0][0]).toEqual('###');
    expect(console.log.mock.calls[1][0]).toEqual('##');
    expect(console.log.mock.calls[2][0]).toEqual('#');
    expect(console.log.mock.calls.length).toEqual(3);
  });
});
