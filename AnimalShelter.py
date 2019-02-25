class myqueue(object):
    def __init__(self):
        self.arr = []

    def enqueue(self,item):
        self.arr.append(item)

    def dequeue(self):
        return self.arr.pop(0)

    def peek(self):
        return self.arr[-1]

class shelter(object):
    def __init__(self):
        self.cat = myqueue()
        self.dog = myqueue()
        self.count = 0

    def enqueue(self,item,type):
        if type == 'dog':
            self.dog.enqueue((item,self.count))
            self.count +=1
        else:
            self.cat.enqueue((item,self.count))
            self.count +=1

    def dequeuecat(self):
        return self.cat.dequeue()

    def dequeuedog(self):
        return self.dog.dequeue()

    def dequeueany(self):
        if self.cat.peek()[1] < self.dog.peek()[1]:
            return self.cat.dequeue()
        else:
            return self.dog.dequeue()



sltr = shelter()
sltr.enqueue('sheru','dog')
sltr.enqueue('tuffy','dog')
sltr.enqueue('catty','cat')
sltr.enqueue('maggi','dog')

print(sltr.dequeuedog())
print(sltr.dequeuedog())
print(sltr.dequeueany())



