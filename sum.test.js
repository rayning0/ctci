function sum(a, b) {
  return a + b;
}

it('adds 1 + 2', () => {
  expect(sum(1, 2)).toBe(3);
})

it('adds 2 negative numbers', () => {
  expect(sum(-1, -2)).toBe(-3);
})
