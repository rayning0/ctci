# https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/validate-parentheses/question?list=neetcode150

# Time: O(n), Space: O(n)
def isValid(s: str) -> bool:
    rparen = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        # c is right paren
        if c in rparen:
            # 1. if stack length > 0 and last stack item is matching left paren, pop it off
            # Ex: stack = "[]{(" and c = ")"
            if len(stack) > 0 and rparen[c] == stack[-1]:
                # "if stack" also means "if len(stack) > 0"
                stack.pop()

            # 2. if stack empty or last stack item is wrong left paren
            # Ex: stack = "" and c = ")"
            # Ex: stack = "[]{(" and c = "}"
            else:
                return False

        # c is left paren
        # Ex: stack = "[]{(" and c = "{"
        else:
            stack.append(c)

    return stack == []


# Tests
if __name__ == "__main__":
    assert isValid("[") == False
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("(]") == False
    assert isValid("([{}])") == True
    assert isValid("([)]") == False
    print("All tests passed!")
