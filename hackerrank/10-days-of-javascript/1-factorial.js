function factorial(n) {
// 	Both factorial functions: O(n) time complexity

  // recursive: O(n) space complexity
  // if (n <= 1) {
  //   return 1;
  // }
  // return n * factorial(n - 1);

  // iterative: O(1) space complexity
  var ans = 1;
  for (var i = 1; i <= n; i++) {
    ans *= i;
  }
  return ans;
}
