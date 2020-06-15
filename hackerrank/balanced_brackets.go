// https://www.hackerrank.com/challenges/balanced-brackets/problem

func isBalanced(s string) string {
    stack := []string{}
    hash := map[string]string{
        "(": ")",
        "[": "]",
        "{": "}",
    }
    var top string

    for _, char := range strings.Split(s, "") {
        if len(stack) > 0 {
            top = stack[len(stack)-1]
        } else {
            top = ""
        }
        if hash[top] == char {
            stack = stack[:len(stack)-1] // pop off stack
        } else {
            stack = append(stack, char)
        }
    }
    if len(stack) > 0 {
        return "NO"
    }
    return "YES"
}
