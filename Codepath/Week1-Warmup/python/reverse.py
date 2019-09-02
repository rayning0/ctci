# Problem: Write a function to reverse a string
def reverse(str):
    chars = list(str)
    s = 0; e = len(chars) - 1
    while s < e:
        chars[e], chars[s] = chars[s], chars[e]
        s += 1
        e -= 1
    return ''.join(chars)
