class Node:
    def __init__(self, data=None, crosspondingData=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None
        self.parent = None
        self.back = None
        self.crossponding = crosspondingData