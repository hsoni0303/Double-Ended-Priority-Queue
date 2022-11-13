from min_heap import MinHeap
from max_heap import MaxHeap

class DoubleEndedQueue:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()
        self.buffer = None
        
    def insert(self, data):
        if self.buffer == None:
            self.buffer = data 
        elif self.buffer > data:
            self.min_heap.insert(data, self.buffer)
            self.max_heap.insert(self.buffer, data)
            self.buffer = None
        else:
            self.max_heap.insert(data, self.buffer)
            self.min_heap.insert(self.buffer, data)
            self.buffer = None
            
    def removeElementAndInsert(self, data):
        crosspondingData = self.min_heap.removeMin()
        self.max_heap.removeElement(crosspondingData)
        self.buffer = crosspondingData
        self.insert(data)
    
    def display(self):
        print("Min Heap")
        self.min_heap.displayTree()
        print("\n")
        print("Max Heap")
        self.max_heap.displayTree()