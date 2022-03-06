// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
// https://leetcode.com/submissions/detail/654472613/
// Runtime: 72 ms, faster than 81.54% of JavaScript online submissions for Best Time to Buy and Sell Stock II.
// Memory Usage: 42.2 MB, less than 45.47% of JavaScript online submissions for Best Time to Buy and Sell Stock II.
// Time to write code: 1:02 min. (Original time to code: 50 min)
// O(n) time, O(1) space
// 3 companies asking this: Amazon, Facebook, Microsoft

/**
 * @param {number[]} prices
 * @return {number}
 */
let maxProfit = function(prices) {
    let profitTotal = 0

    for (let i = 0; i < prices.length - 1; i++) {
        if (prices[i] < prices[i + 1]) {
            profitTotal = profitTotal + prices[i + 1] - prices[i]
        }
    }

    return profitTotal
}
