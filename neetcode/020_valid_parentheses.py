# https://leetcode.com/problems/valid-parentheses/description/
# https://neetcode.io/solutions/valid-parentheses
# Stack

# Time: O(n), Space: O(n)
def isValid(s: str) -> bool:
    rparen = {')':'(', ']':'[', '}':'{'}
    stack = []

    for c in s:
        if c in rparen:
            # 1. if stack length > 0 and top stack item is matching left paren, pop it off
            # Ex: stack = "[]{(" and c = ")"
            if stack and rparen[c] == stack[-1]:
                stack.pop()

            # 2. stack is empty or top stack item is wrong left paren
            # Ex: stack = "" and c = ")"
            # Ex: stack = "[]{(" and c = "}"
            else:
                return False

        # c is left paren
        # Ex: stack = "[]{(" and c = "{"
        else:
            stack.append(c)

    return stack == []

if __name__ == "__main__":
    assert isValid("[") == False
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("(]") == False
    assert isValid("([{}])") == True
    assert isValid("([)]") == False
    print("All tests passed!")
