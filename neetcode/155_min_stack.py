# https://leetcode.com/problems/min-stack/description/
# https://neetcode.io/solutions/min-stack
#

# Design stack that supports push, pop, top, and retrieving minimum element in constant time.
# Each function MUST have O(1) time.

# PLAN: Make 2 stacks s and min. s stores all values added. min stores min value pushed in s so far.
# When we pop s, we must also pop min.

# 1. 2 Stacks: Easy to remember for interview!
# Overall storage: O(n)
class MinStack:
    def __init__(self):
        self.s = []

        # min = list of min values pushed in s so far.
        # s =   [-2,  0, -3,  4, -6... new value]
        # min = [-2, -2, -3, -3, -6... min value so far in s]
        self.min = []

    # Time: O(1), Space: O(1) auxiliary
    def push(self, value: int) -> None:
        self.s.append(value)
        if not self.min:
            self.min.append(value)
        else:
            min_so_far = self.min[-1]
            self.min.append(min(min_so_far, value))

    # Time: O(1), Space: O(1)
    def pop(self) -> None:
        self.min.pop()
        return self.s.pop()

    # Time: O(1), Space: O(1)
    def top(self) -> int:
        return self.s[-1]

    # Time: O(1), Space: O(1)
    def getMin(self) -> int:
        return self.min[-1]

# 2. 2 Stacks (Optimized for space). Harder to remember.
# Q: "Can you reduce space used?"
# A: "Push to min stack ONLY if new value ≤ the current min, saving space in average case. Worst case stays O(n). Rule: push to min with ≤, pop from min ONLY when popped s value == current min."

# class MinStack:
#     def __init__(self):
#         self.s = []
#         self.min = []

#     def push(self, value: int) -> None:
#         self.s.append(value)
#         # Push to min stack if empty OR value <= current min
#         if not self.min or value <= self.min[-1]:
#             self.min.append(value)

#     def pop(self) -> None:
#         val = self.s.pop()
#         # Pop from min stack only if it matches current min
#         if val == self.min[-1]:
#             self.min.pop()

#     def top(self) -> int:
#         return self.s[-1]

#     def getMin(self) -> int:
#         return self.min[-1]

if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(f"s: {obj.s}, min: {obj.min}")
    assert obj.getMin() == -3

    obj.pop()
    assert obj.top() == 0
    print(f"s: {obj.s}, min: {obj.min}")
    assert obj.getMin() == -2

    obj.push(4)
    print(f"s: {obj.s}, min: {obj.min}")
    assert obj.getMin() == -2

    obj.push(-5)
    obj.push(6)
    print(f"s: {obj.s}, min: {obj.min}")
    assert obj.getMin() == -5
    print("All tests passed!")

# s: [-2, 0, -3],       min: [-2, -2, -3]
# s: [-2, 0],           min: [-2, -2]
# s: [-2, 0, 4],        min: [-2, -2, -2]
# s: [-2, 0, 4, -5, 6], min: [-2, -2, -2, -5, -5]
