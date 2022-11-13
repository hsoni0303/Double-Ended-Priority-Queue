from node import Node
class MinHeap:
    def __init__(self):
        self.head = None

    def insert(self, data, crosspondingData):
        
        newNode = Node(data, crosspondingData)
        if self.head == None:
            self.head = newNode
            return
        
        node = self.head
        while (node.left and node.right) is not None:
            node = node.next
            
        temp = node
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.back = temp
        newNode.parent = node
        
        if node.left == None:
            node.left = newNode
        elif node.right == None:
            node.right = newNode
            
        # heapify to put new node at its right position
        self.heapify(newNode)
        
    def heapify(self, node):
        # comparing upwards and swapping if property not following
        if node == None:
            return
        while node.parent is not None:
            if node.data < node.parent.data:
                nodeData = node.data
                crosspondingData = node.crossponding
                
                node.data = node.parent.data
                node.crossponding = node.parent.crossponding
                
                node.parent.data = nodeData
                node.parent.crossponding = crosspondingData
                
            elif node.data >= node.parent.data:
                break
                
        self.heapify(node.parent)
        
    def adjustMin(self, node):
        if node == None or (node.left == None and node.right == None):
            return None
        if node.left != None and node.right == None:
            if node.left.data < node.data:
                temp = node.data
                node.data = node.left.data
                node.left.data = temp
                
                temp = node.crossponding
                node.crossponding = node.left.crossponding
                node.left.crossponding = temp
                
        else:
            if node.left.data < node.right.data:
                if node.left.data < node.data:
                    temp = node.left.data
                    node.left.data = node.data
                    node.data = temp
                    
                    temp = node.crossponding
                    node.crossponding = node.left.crossponding
                    node.left.crossponding = temp
                    
                    if node.left:
                        self.adjustMin(node.left)
                        
            else:
                if node.right.data < node.data:
                    temp = node.right.data
                    node.right.data = node.data
                    node.data = temp

                    temp = node.crossponding
                    node.crossponding = node.right.crossponding
                    node.right.crossponding = temp

                    if node.right:
                        self.adjustMin(node.right)

        
    def displayTree(self):
        # Level Order Tree Traversal Printing
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
            
    def displayCrosspondingTree(self):
        temp = self.head
        while temp is not None:
            print(temp.crossponding)
            temp = temp.next
            
    def removeMin(self):
        if self.head == None:
            print("List Empty")
            return
        temp = self.head
        minCrossponding = temp.crossponding
        if temp.next == None:
            self.head = None
            return minCrossponding
        
        while temp.next is not None:
            temp = temp.next
        
        if temp.data == self.head.data:
            self.head = None
            return
        
        last = temp
        secondLast = temp.back
        
        if self.head == last:
            self.head = None
        else:
            if last.parent.right:
                temp = last.back
                self.head.data = last.data
                self.head.crossponding = last.crossponding
                last.parent.right = None
                last.back.next = None
                
            else:
                temp = last.back
                self.head.data = last.data
                self.head.crossponding = last.crossponding
                last.parent.left = None
                last.back.next = None
                
        self.adjustMin(self.head)
        return minCrossponding