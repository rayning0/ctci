# Problem: Given a Queue data structure that supports standard operations like enqueue() and dequeue(),
# implement a Stack data structure using only instances of Queue and queue operations allowed on the instances.
import queue
class MyStack:
    q1 = queue.Queue()
    q2 = queue.Queue()
    top = -1

    def push(self, x):
        self.q1.put(x);
        self.top = x;

    def pop(self):
        while (self.q1.qsize() > 1):
            self.top = self.q1.get()
            self.q2.put(self.top)
        self.q1.get();
        temp = self.q1;
        self.q1 = self.q2;
        self.q2 = temp;

    def top(self):
        return top

    def empty(self):
        return self.q1.empty()
