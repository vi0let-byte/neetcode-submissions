class DynamicArray:
    
    def __init__(self, capacity: int):
        self.data = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.data[i]


    def set(self, i: int, n: int) -> None:
        self.data[i] = n


    def pushback(self, n: int) -> None:
        if(len(self.data) >= self.capacity):
            self.resize()
        self.data.append(n)


    def popback(self) -> int:
        n = self.data.pop()
        return n

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return len(self.data)
        
    
    def getCapacity(self) -> int:
        return self.capacity
