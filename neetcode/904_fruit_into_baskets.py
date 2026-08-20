# https://leetcode.com/problems/fruit-into-baskets/description/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://neetcode.io/solutions/fruit-into-baskets
# Variable Sliding Window
# Basically: "Find longest subarray with at most 2 distinct values"

# Time: O(n), Space: O(1) <--- since freq only has max of 2 keys
def totalFruit(fruits: list[int]) -> int:
    l = max_length = 0
    freq = {}

    for r in range(len(fruits)):
        freq[fruits[r]] = freq.get(fruits[r], 0) + 1

        # Shrink window from left till we have at most 2 distinct types
        while len(freq.keys()) > 2:
            freq[fruits[l]] -= 1
            if freq[fruits[l]] == 0:
                del freq[fruits[l]]
            l += 1

        length = r - l + 1
        max_length = max(max_length, length)

    return max_length

if __name__ == "__main__":
    assert totalFruit([1, 2, 1]) == 3
    assert totalFruit([0, 1, 2, 2]) == 3
    assert totalFruit([1, 2, 3, 2, 2]) == 4
    assert totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    print("All tests passed!")

# For fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]:

# freq: {3: 1}, l: 0, r: 0
# length: 1, max length: 0
# freq: {3: 2}, l: 0, r: 1
# length: 2, max length: 1
# freq: {3: 3}, l: 0, r: 2
# length: 3, max length: 2
# freq: {3: 3, 1: 1}, l: 0, r: 3
# length: 4, max length: 3
# freq: {3: 3, 1: 1, 2: 1}, l: 0, r: 4
# freq: {3: 2, 1: 1, 2: 1}, l: 1, r: 4
# freq: {3: 1, 1: 1, 2: 1}, l: 2, r: 4
# freq: {1: 1, 2: 1}, l: 3, r: 4
# length: 2, max length: 4
# freq: {1: 2, 2: 1}, l: 3, r: 5
# length: 3, max length: 4
# freq: {1: 3, 2: 1}, l: 3, r: 6
# length: 4, max length: 4
# freq: {1: 3, 2: 2}, l: 3, r: 7
# length: 5, max length: 4
# freq: {1: 3, 2: 2, 3: 1}, l: 3, r: 8
# freq: {1: 2, 2: 2, 3: 1}, l: 4, r: 8
# freq: {1: 2, 2: 1, 3: 1}, l: 5, r: 8
# freq: {1: 1, 2: 1, 3: 1}, l: 6, r: 8
# freq: {2: 1, 3: 1}, l: 7, r: 8
# length: 2, max length: 5
# freq: {2: 1, 3: 2}, l: 7, r: 9
# length: 3, max length: 5
# freq: {2: 1, 3: 2, 4: 1}, l: 7, r: 10
# freq: {3: 2, 4: 1}, l: 8, r: 10
# length: 3, max length: 5
