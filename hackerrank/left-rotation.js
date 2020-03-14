// Both are same:
// https://www.hackerrank.com/challenges/array-left-rotation/problem
// https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

function leftRotation(a, d) {
  if (d == a.length) {
    return a;
  }
  return a.slice(d).concat(a.slice(0, d));
}
