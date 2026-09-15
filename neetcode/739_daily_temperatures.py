# https://leetcode.com/problems/daily-temperatures/description/
# https://neetcode.io/solutions/daily-temperatures
# Monotonic Stack: elements always in sorted order

# PLAN: Use stack to store (temp, index) pairs for each day we have NOT yet found a warmer day.
# 1. For each current temp, WHILE len(stack) > 0 and current temp > temp on top of stack (i.e. we found a warmer day), do loop:
#   a. pop (temp, index) pair
#   b. answer[index] = current index - index (# of days after ith day to get warmer temp)
# 2. Add (current temp, index) to stack.

# Temps in descending order always have same "answer" day.

# Time: O(n), Space: O(n)
# Why time is O(n) despite the nested loop? Each element is pushed + popped at most ONCE, so total operations are bounded by 2n.
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    answer = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        # Keep popping stack till current day's temp is not warmer than temp at top of stack
        while stack and t > stack[-1][0]:
            stack_t, stack_i = stack.pop()
            answer[stack_i] = i - stack_i

        # Store (temp, index) pairs for each day which has NOT yet found a warmer day.
        # This creates a "monotonic decreasing stack," since values like: [(75, 2), (71, 3), (69, 4)] all haven't seen a warmer day.
        stack.append((t, i))

    return answer

if __name__ == "__main__":
    assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert dailyTemperatures([30,40,50,60]) == [1,1,1,0]
    assert dailyTemperatures([30,60,90]) == [1,1,0]
    assert dailyTemperatures([30,38,30,36,35,40,28]) == [1,4,1,2,1,0,0]
    assert dailyTemperatures([22,21,20]) == [0,0,0]
    print("All tests passed!")

# Ex: temperatures = [73,74,75,71,69,72,76,73]

# stack: [(73, 0)]
# Temp 74 > Temp 73. It took 1 days to find a warmer day.
# answer: [1, 0, 0, 0, 0, 0, 0, 0]
# stack: [(74, 1)]
# Temp 75 > Temp 74. It took 1 days to find a warmer day.
# answer: [1, 1, 0, 0, 0, 0, 0, 0]
# stack: [(75, 2)]
# stack: [(75, 2), (71, 3)]
# stack: [(75, 2), (71, 3), (69, 4)]
# Temp 72 > Temp 69. It took 1 days to find a warmer day.
# answer: [1, 1, 0, 0, 1, 0, 0, 0]
# Temp 72 > Temp 71. It took 2 days to find a warmer day.
# answer: [1, 1, 0, 2, 1, 0, 0, 0]
# stack: [(75, 2), (72, 5)]
# Temp 76 > Temp 72. It took 1 days to find a warmer day.
# answer: [1, 1, 0, 2, 1, 1, 0, 0]
# Temp 76 > Temp 75. It took 4 days to find a warmer day.
# answer: [1, 1, 4, 2, 1, 1, 0, 0]
# stack: [(76, 6)]
# stack: [(76, 6), (73, 7)]
