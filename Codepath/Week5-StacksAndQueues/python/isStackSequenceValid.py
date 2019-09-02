# Given push and pop sequences with distinct values, check if this could have been the result of a sequence of push and pop operations on an initially empty stack.
#
# Example:
# Input: pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
# Output: True
#
# Following sequence can be performed:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
# pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
# Output: False
#
#  Expanation: 1 can't be popped before 2.
def isStackSequenceValid(pushed, popped):
    if len(pushed) != len(popped):
        return False
    j = 0
    stack = []

    for x in pushed:
        stack.append(x)

        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j = j + 1

    return j == len(popped)
