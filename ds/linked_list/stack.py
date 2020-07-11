class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self,data):
        headNode = Node(data)
        self.head = headNode
        self.tail = headNode
        
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def pop(self):
        data = self.head
        self.head = self.head.next
        return data.data
    
    def showStack(self):
        current = self.head
        while current:
            print(current.data,end=" --> ")
            current = current.next
        print("\n")
            
stack = Stack(99)

stack.push(56)
stack.push(36)
stack.push(16)
stack.push(43)

stack.showStack()

print(stack.pop())

stack.showStack()