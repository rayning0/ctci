// https://www.hackerrank.com/challenges/ctci-coin-change/problem

function main() {
  var n_temp = readLine().split(' ');
  var n = parseInt(n_temp[0]); //target sum
  var m = parseInt(n_temp[1]); //# of coins
  coins = readLine().split(' ');
  coins = coins.map(Number);

  let ways = new Array(n + 1).fill(0);
  ways[0] = 1;
  coins.forEach((coin) => {
    for (let sum = coin; sum <= n; sum++) {
      ways[sum] += ways[sum - coin];
    }
  });
  console.log(ways[n]);
}
