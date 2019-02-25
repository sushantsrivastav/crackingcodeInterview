#Stacks: Implement a MyQueue class which implements a queue using two stacks.
class myqueue(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enquque(self,item):
        self.instack.append(item)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()

    def peek(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]

q = myqueue()
q.enquque(3)
q.enquque(4)
q.enquque(6)
print(q.dequeue())
print (q.peek())
print(q.dequeue())
