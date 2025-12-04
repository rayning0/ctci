# https://leetcode.com/problems/merge-intervals/description/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://neetcode.io/problems/merge-intervals/question?list=neetcode150

# Time: O(n log n), Space: O(n)
def merge(intervals: list[list[int]]) -> list[list[int]]:
    ints = sorted(intervals)
    res = []
    for int in ints:
        # if res == [] or if NO OVERLAP! Ex: res = [[2,6]], int = [8,10]
        # Meaning: If 2nd val of last item of res < 1st value of int
        if not res or res[-1][1] < int[0]:
            res.append(int)
        else:  # OVERLAP! Ex: [[1,3]], int = [2,6] => New res = [[1, 6]]
            # Change 2nd val of last item of res to max of it and 2nd val of int. Ex: max(3, 6) = 6.
            res[-1][1] = max(res[-1][1], int[1])

    return res


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[4, 7], [1, 4]]) == [[1, 7]]
    assert merge([[1, 4]]) == [[1, 4]]
    print("All tests passed!")
