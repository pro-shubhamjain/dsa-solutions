const { countCharSerlize, countAllChar } = require('./characterCount');

test('countCharSerlize compresses repeated chars with counts', () => {
  expect(countCharSerlize('abbbccddddaab')).toEqual('a1b3c2d4a2b1');
});

test('countCharSerlize handles single character', () => {
  expect(countCharSerlize('aaa')).toEqual('a3');
});

test('countAllChar counts frequency of each character', () => {
  const result = countAllChar('aabbbc');
  expect(result.a).toEqual(2);
  expect(result.b).toEqual(3);
  expect(result.c).toEqual(1);
});
