# https://leetcode.com/problems/implement-queue-using-stacks/description/
# https://neetcode.io/solutions/implement-queue-using-stacks

# You may ONLY use these standard operations of a stack!
# 1. push to top:                   list.append(x)
# 2. pop from top:                  list.pop()
# 3. peek at top:                   list[-1]
# 3. size:                          len(list)
# 4. is_empty ops are valid.        len(list) == 0 or "not list"
# You may only operate on RIGHT END of each list. No "list[0]", "del list[0]", or "insert(0, x)".

# PLAN: Use 2 stacks s1, s2. Change s2 to have behavior of a queue. Create s2 by reversing s1.

# 1. 2 Stacks (Optimized. Amortized time.)

# Instead of moving all elements back from s2 to s1 after each pop/peek, keep them in s2.
# s1 handles incoming elements (push), while s2 holds elements in reversed order for pop/peek.
# KEY: Only if s2 is empty, then move all elements from s1 to s2!
# Each element gets moved at most twice: once to s2, once when popped. This gives amortized O(1) time for pop/peek.

class MyQueue:
    # Time: O(1), Space: O(1)
    def __init__(self):
        self.s1, self.s2 = [], []

    # Time: O(1), Space: O(n)
    def push(self, x: int) -> None:
        self.s1.append(x)

    # Time: O(1) amortized, Space: O(1) auxiliary
    def pop(self) -> int:
        # To avoid moving all elements back from s2 to s1, only empty s1 if s2 is empty.
        if not self.s2:
            # Ex: s1 = [1,2,3]
            # Reverses and empties s1 to make s2 = [3,2,1]
            # Now top of s1 (3) == first element of queue s2 (3)
            while self.s1:
                self.s2.append(self.s1.pop())

        # Pops first element from queue s2. This is same as deleting bottom of stack s1.
        return self.s2.pop()

    # Time: O(1) amortized, Space: O(1) auxiliary
    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]   # Same code as pop() function, except this line.

    # Time: O(1), Space: O(1)
    # Check BOTH s1 and s2 are empty. The combo of s1 and s2 = the whole queue of elements.
    def empty(self) -> bool:
        return not self.s1 and not self.s2

Q: Why in pop/peek functions do we ONLY move all elements from s1 to s2 if s2 is empty?

A: Since s2 already reversed s1 and acts like a queue, until s2 is empty,
even if we later add new elements to s1, we can keep popping new elements from s2 without touching s2.
Only if s2 is empty and s1 has new elements do we need to again reverse new elements of s1 to simulate a queue.

Example:
push(1), push(2), push(3), pop(), pop()
After the pushes:

s1: [1, 2, 3]  (3 is top)
s2: []
First pop() → s2 is empty, so transfer all elements from s1 to s2:

s1: []
s2: [3, 2, 1]  (1 is top, correct FIFO order!)
Pop returns 1 ✓

Second pop() → s2 is not empty, so we just pop from s2:

s2: [3, 2]  (2 is top)
Pop returns 2 ✓

Imagine we wrongly transferred all elements from s1 to s2 each time.
After the first pop, suppose we pushed 4, then transferred immediately:

s1: [4]  → transfer to s2 →  s2: [2, 3, 4]  (4 is top)
Next pop would return 4 ✗ — but it should return 3! The FIFO order is broken because newer elements from s1 got placed on top of older elements still waiting in s2.

Key: s2 always holds older elements in correct FIFO order. New elements in s1 must wait till all older elements in s2 are popped before they get their turn.
____________________
# 2. 2 Stacks (Brute Force). Inefficient, since each pop/peek requires moving all elements twice.
# class MyQueue:
#     # Time: O(1)
#     def __init__(self):
#         self.s1, self.s2 = [], []

#     # Time: O(1)
#     def push(self, x: int) -> None:
#         self.s1.append(x)

#     # Time: O(n), Space: O(n)
#     def pop(self) -> int:
#         # Ex: s1 = [1,2,3]
#         # Reverses and empties s1 to make s2 = [3,2,1]
#         # Now top of s1 (3) == first element of queue s2 (3)
#         while self.s1:
#             self.s2.append(self.s1.pop())

#         ans = self.s2.pop()   # Pops first element from queue s2, same as deleting bottom of stack s1.

#         # Reverses and empties s2 to remake s1 again, minus popped element: s1 = [2,3]
#         while self.s2:
#             self.s1.append(self.s2.pop())

#         return ans

#     # Time: O(n), Space: O(n)
#     def peek(self) -> int:
#         while self.s1:
#             self.s2.append(self.s1.pop())

#         ans = self.s2[-1]   # Same code as pop() function, except this line.

#         while self.s2:
#             self.s1.append(self.s2.pop())

#         return ans

#     # Time: O(1)
#     def empty(self) -> bool:
#         return not self.s1

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    assert obj.s1 == [1, 2]
    assert obj.peek() == 1
    assert obj.pop() == 1
    assert obj.s2 == [2]
    assert obj.empty() == False

    obj = MyQueue()
    obj.push(5)
    assert obj.empty() == False
    print("All tests passed!")
