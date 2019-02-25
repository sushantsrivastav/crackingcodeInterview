import ctypes
class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def make_array(self,capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError("index out of range")
        return self.A[index]

    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = ele
        self.n += 1

    def _resize(self,new_capacity):
        B = self.make_array(new_capacity)

        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_capacity



arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))