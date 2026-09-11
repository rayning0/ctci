# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# https://neetcode.io/solutions/evaluate-reverse-polish-notation
# Stack

# Time: O(n), Space: O(n)
def evalRPN(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token in '+-*/':
            n1, n2 = stack[-2], stack[-1]

            match token:
                case '+':
                    stack.pop()
                    stack.pop()
                    stack.append(n1 + n2)
                case '-':
                    stack.pop()
                    stack.pop()
                    stack.append(n1 - n2)
                case '*':
                    stack.pop()
                    stack.pop()
                    stack.append(n1 * n2)

        # "Division between 2 integers always truncates toward 0. There will not be any division by 0."
        # Ex: 7/3 = 2.333 truncates to 2. -7/3 = -2.333 truncates to -2.
        # Only cuts off decimal. Does not round to nearest integer.
                case '/':
                    stack.pop()
                    stack.pop()
                    stack.append(int(n1 / n2))
        else:
            stack.append(int(token))

    return stack[-1]


if __name__ == "__main__":
    assert evalRPN(["2","1","+","3","*"]) == 9
    assert evalRPN(["4","13","5","/","+"]) == 6
    assert evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
    assert evalRPN(["1","2","+","3","*","4","-"]) == 5
    assert evalRPN(["18"]) == 18
    print("All tests passed!")
