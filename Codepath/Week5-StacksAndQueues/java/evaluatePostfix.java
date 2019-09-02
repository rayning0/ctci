/*
 * Problem: Write a function to evaluate the value of an expression in postfix notation represented by a string with numbers between 0 and 9 and operators separated by whitespace. The expression supports 4 binary operators ‘+’, ‘*’, ‘-’ and ‘/’
 *
 * Example:
 * Input: "5 1 2  +  4  * +  3  -"
 * Output: 14

 * The expression is evaluated as follows:
    5 3 4 * + 3 -
    5 12 + 3 -
    17 3 -
    14
*/
public int evaluatePostfix(String exp) {
	Stack<Integer> stack = new Stack<>();

	for(int i = 0; i < exp.length(); i++) {
	    char c = exp.charAt(i);
	    if (Character.isDigit(c)) {
	        stack.push(c - '0');
        } else if (Character.isSpace(c)) {
            continue;
        } else {
	     int val1 = stack.pop();
	     int val2 = stack.pop();
	     switch(c) {
	         case '+':
	         stack.push(val2 + val1);
	         break;

	         case '-':
	         stack.push(val2 - val1);
	         break;

	         case '/':
	         stack.push(val2 / val1);
	         break;

	         case '*':
	         stack.push(val2 * val1);
	         break;
	       }
	    }
	}
