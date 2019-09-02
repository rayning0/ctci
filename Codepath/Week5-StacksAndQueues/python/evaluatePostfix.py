# Problem: Write a function to evaluate the value of an expression in postfix notation represented by a string with numbers between 0 and 9 and operators separated by whitespace. The expression supports 4 binary operators ‘+’, ‘*’, ‘-’ and ‘/’
#
# Example:
# Input: "5 1 2  +  4  * +  3  -"
# Output: 14
#
# The expression is evaluated as follows:
#     5 3 4 * + 3 -
#     5 12 + 3 -
#     17 3 -
#     14
def evaluatePostfix(exp):
 stack = []
 # Iterate over the expression for conversion
 for i in exp:
     if i.isdigit():
         stack.append(i)
     elif i.isspace():
        continue
     else:
         val1 = stack.pop()
         val2 = stack.pop()
         stack.append(str(eval(val2 + i + val1)))

 return int(stack.pop())
