# https://leetcode.com/problems/sum-of-square-numbers/description/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://algo.monster/liteproblems/633
# 2 pointers

# Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.
# Possible answers: a == b, a or b == 0

import math


# Time: O(sqrt c), Space: O(1)
def judgeSquareSum(c: int) -> bool:
    l, r = 0, round(math.sqrt(c))
    while l <= r:
        sum = l * l + r * r
        if sum < c:
            l += 1
        elif sum > c:
            r -= 1
        else:
            return True
    return False


if __name__ == "__main__":
    assert judgeSquareSum(5) == True
    assert judgeSquareSum(3) == False
    assert judgeSquareSum(0) == True
    assert judgeSquareSum(2) == True
    assert judgeSquareSum(29) == True
    assert judgeSquareSum(4) == True
    assert judgeSquareSum(28) == False
    assert judgeSquareSum(11) == False
    assert judgeSquareSum(13) == True
    print("All tests passed!")
