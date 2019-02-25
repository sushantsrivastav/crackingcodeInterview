class stack(object):
    def __init__(self):
        self.arr= []
        self.min = None

    def isempty(self):
        return self.arr == []

    def push(self,item):
        if self.isempty():
            self.arr.append(item)
            self.min = item
            print("number inserted" + str(item))
            return
        if item < self.min:
            self.arr.append(2*item - self.min)
            self.min = item
        else:
            self.arr.append(item)
        print("number isnerted" + str(item))

    def pop(self):
        if self.isempty():
            print("stack is empty")
            return
        pop_item = self.arr.pop()
        if pop_item < self.min:
            print(self.min)
            self.min = 2*self.min - pop_item
        else:
            print(pop_item)

    def getMin(self):
        print(self.min)

    def peek(self):
        item = self.arr[-1]
        if item < self.min:
            print(self.min)
        else:
            print(item)

s = stack()
s.push(3)
s.push(5)
s.getMin()
s.push(2)
s.push(1)
s.getMin()
s.pop()
s.getMin()
s.pop()
s.peek()