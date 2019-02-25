class BinaryHeap(object):
    def __init__(self):
        self.heplist = [0]
        self.currentsize = 0

    def insert(self,k):
        self.heplist.append(k)
        self.currentsize += 1
        self.percUp(self.currentsize)

    def percUp(self,i):
        while i//2 > 0:
            if self.heplist[i] < self.heplist[i//2]:
                temp = self.heplist[i//2]
                self.heplist[i//2] = self.heplist[i]
                self.heplist[i] = temp
            i = i //2

    def delMin(self):
        retval = self.heplist[1]
        self.heplist[1] = self.heplist[self.currentsize]
        self.currentsize -= 1
        self.heplist.pop()
        self.percdown(1)

    def percDown(self,i):
        while i*2 <= self.currentsize:
            mc = self.minChild(i)
            if self.heplist[i] > self.heplist[mc]:
                temp = self.heplist[mc]
                self.heplist[mc] = self.heplist[i]
                self.heplist[i] = temp
            i = mc
    def minChild(self,i):
        if (i*2) + 1 > self.currentsize:
            return i*2
        else:
            if self.heplist[(i*2) + 1] > self.heplist[i*2]:
                return i * 2
            else :
                return (i*2) + 1
