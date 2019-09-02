/*
 * Problem: Given push and pop sequences with distinct values, check if this could have been the result of a sequence of push and pop operations on an initially empty stack.
 * Example:
 * Input: pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
 * Output: True

 * Following sequence can be performed:
 * push(1), push(2), push(3), push(4), pop() -> 4,
 * push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

 * pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
 * Output: False

 * Explanation: 1 can't be popped before 2.
*/
boolean isStackSequenceValid(int pushed[], int popped[])
{
    if(pushed.length != popped.length)
        return false;
    int len = pushed.length;

    int j = 0;
    Stack<Integer> st = new Stack<>();

    for (int i = 0; i < pushed.length; i++) {
        st.push(pushed[i]);
        while (!st.empty() && j < len &&
                st.peek() == popped[j]) {
            st.pop();
            j++;
        }
    }
    return j == len;
}
