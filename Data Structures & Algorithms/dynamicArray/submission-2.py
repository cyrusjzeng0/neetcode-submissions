class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity # initialize empty null array with capacity number of elements 
        self.capacity = capacity
        self.size = 0 # keep track of number of used array elements

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity: 
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        val = self.arr[self.size]
        self.arr[self.size] = None
        return val

    def resize(self) -> None:
        temp = self.arr # temporary arr to hold values currently in arr
        self.arr = [None] * self.capacity * 2 # re-initialize arr as null arr with twice as many elements
        for i in range(self.capacity):
            self.arr[i] = temp[i]
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity