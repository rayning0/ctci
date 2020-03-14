// Both are same:
// https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
// https://www.hackerrank.com/challenges/array-left-rotation/problem

function main() {
  var n_temp = readLine().split(' ');
  var n = parseInt(n_temp[0]);
  var k = parseInt(n_temp[1]);
  a = readLine().split(' ');
  a = a.map(Number);
  let ans;
  if (k == n) {
    ans = a;
  }
  ans = a.slice(k).concat(a.slice(0, k));
  console.log(ans.join(' '));
}
