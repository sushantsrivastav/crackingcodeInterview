class stackPlate(object):
    def __init__(self,threshold):
        self.threshold = threshold
        self.arr = []
        self.arr_ref = [self.arr]

    def push(self,item):
        last_array = self.arr_ref[-1]
        if len(last_array) == self.threshold:
            arr = []
            self.arr_ref.append(arr)
        self.arr_ref[-1].append(item)
        print("item inserted " + str(item))

    def pop(self):
        item = self.arr_ref[-1].pop()
        if len(self.arr_ref[-1]) == 0:
            self.arr_ref.pop()
        print(item)


s = stackPlate(3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.pop()
s.pop()