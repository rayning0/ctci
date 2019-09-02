/*
 * Problem: Implement a queue using instances of stack data structure and operations on them.
*/
class MyQueue {
    private Stack<Integer> s1 = new Stack<>();
    private Stack<Integer> s2 = new Stack<>();
    private int front;

    /** Push element x to the back of queue. */
    public void enQueue(int x) {
         if (s1.empty())
            front = x;
        s1.push(x);
    }

    /** Removes the element from in front of queue
     * and returns that element. */
    public int deQueue() {
        if (s2.isEmpty()) {
            while (!s1.isEmpty())
                s2.push(s1.pop());
        }
        return s2.pop();
    }

    public int peek() {
        if (!s2.isEmpty()) {
            return s2.peek();
        }
        return front;
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
    }
