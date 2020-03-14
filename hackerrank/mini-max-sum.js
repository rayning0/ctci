// https://www.hackerrank.com/challenges/mini-max-sum/problem

function miniMaxSum(arr) {
  const reducer = (accumulator, currentValue) => accumulator + currentValue;
  const total = arr.reduce(reducer);
  let min = max = total - arr[0];
  arr.forEach((num) => {
    let sum = total - num;
    if (sum > max) {
      max = sum;
    } else if (sum < min) {
      min = sum;
    }
  });
  console.log(`${min} ${max}`);
}
