const { calc, alternative, closure, closureFixed } = require('./currying');

test('calc curries four operations and returns a final function', () => {
  // (10 - 5) * 20 / 2 = 50
  const result = calc()(10)(5)(20)(2)();
  expect(result).toEqual(50);
});

test('alternative (fluent chainable API) computes the same kind of result', () => {
  // ((0 + 5 - 2) * 10) / 2 = 15
  const result = alternative().add(5).sub(2).multiply(10).divided(2).getResult();
  expect(result).toEqual(15);
});

test('closure is a function', () => {
  expect(typeof closure).toEqual('function');
});

test('closureFixed is a function', () => {
  expect(typeof closureFixed).toEqual('function');
});

test('closure (var, but with i passed as a function argument) prints values correctly: 0, 1, 2', done => {
  const logged = [];
  const originalLog = console.log;
  console.log = (val) => logged.push(val);

  closure();

  setTimeout(() => {
    console.log = originalLog;
    // NOT [3, 3, 3] -- passing i as print's parameter creates a fresh
    // binding per call, so this avoids the classic var-in-loop bug.
    expect(logged).toEqual([0, 1, 2]);
    done();
  }, 10);
});

test('closureFixed (let, inline arrow) also prints values correctly: 0, 1, 2', done => {
  const logged = [];
  const originalLog = console.log;
  console.log = (val) => logged.push(val);

  closureFixed();

  setTimeout(() => {
    console.log = originalLog;
    expect(logged).toEqual([0, 1, 2]);
    done();
  }, 10);
});
