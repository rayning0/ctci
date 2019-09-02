# Problem: Implement a queue using instances of stack data structure and operations on them.
class MyQueue:

    s1 = []
    s2 = []
    front = -1

    def enQueue(self, x):
        if (len(self.s1) == 0):
            front = x
        self.s1.append(x)

    def deQueue(self):
        if len(self.s2) == 0:
            while(len(self.s1) != 0):
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if len(self.s2) != 0:
            return self.s2[0]
        return self.front

    def empty(self):
        return len(self.s2) == 0 and len(self.s1) == 0
