# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/buy-and-sell-crypto/question
# Use sliding window

# Time: O(n), Space: O(1)
def maxProfit(prices: list[int]) -> int:
    l, max_profit = 0, 0

    for r in range(1, len(prices)):
        if prices[l] > prices[r]:
            l = r
        else:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

    return max_profit


if __name__ == "__main__":
    assert maxProfit([2]) == 0
    assert maxProfit([2, 1, 4]) == 3
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert maxProfit([7, 6, 4, 3, 1]) == 0
    assert maxProfit([10, 1, 5, 6, 7, 1]) == 6
    assert maxProfit([10, 8, 7, 5, 2]) == 0
    print("All tests passed!")

# [7,1,5,3,6,4]
# maxp = 0
# l, r = 0, 1
# compare 7, 1
# p[l] > p[r]

# l = r = 1
# r += 1 = 2

# compare 1, 5
# p[l] < p[r]
# profit = 5-1 = 4
# maxp = max(0, 4) = 4
# r += 1 = 3

# compare 1, 3
# p[l] < p[r]
# profit = 3-1 = 2
# maxp = max(4, 2) = 4
# r += 1 = 4

# compare 1, 6
# p[l] < p[r]
# profit = 6-1 = 5
# maxp = max(4, 5) = 5
# r += 1 = 5
# -------------------
# [7, 6, 4, 3, 1]
# maxp = 0
# l, r = 0, 1
# compare 7, 6
# p[l] > p[r]
# l = r = 1
# r += 1 = 2

# compare 6, 4
# p[l] > p[r]
# l = r = 2
# r += 1 = 3

# etc....
# maxp = 0
