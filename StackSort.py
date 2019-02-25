class stack(object):
    def __init__(self):
        self.arr = []

    def push(self,item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[-1]

    def isempty(self):
        return self.arr == []

    def size(self):
        return len(self.arr)

def stack_sort(s):
    r = stack()
    while not s.isempty():
        temp = s.pop()
        while not r.isempty() and r.peek() > temp:
            s.push(r.pop())
        r.push(temp)
    return r


s = stack()
s.push(10)
s.push(2)
s.push(9)
s.push(4)
print(s.size)
s = stack_sort(s)
for i in range(s.size()):
    print(s.pop())