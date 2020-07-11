#Nodes are added from tail and removed from head

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self,head):
        self.head = head
        self.tail = head
        
    def enqueue(self,data):
        newNode = Node(data)
        if self.tail != None:
            self.tail.next = newNode 
        self.tail = newNode
        if self.head == None:
            self.head = newNode
    
    def dequeue(self):
        if self.head == None:
            return ("NO ELEMENTS ARE AVAILABLE TO DEQUEUE")
        else:
            deq = self.head
            self.head = self.head.next
            return deq.data
        
    def showQueue(self):
        current = self.head
        while current:
            print(current.data, end = "->")
            current = current.next
        print("\n")
            
   
head = Node(99)         
queue = Queue(head)
newNode_1 = Node(69)
queue.enqueue(89)
queue.enqueue(45)
queue.enqueue(576)
queue.showQueue()

print("DEQUEUE : ",queue.dequeue())
print("DEQUEUE : ",queue.dequeue())
print("DEQUEUE : ",queue.dequeue())
print("DEQUEUE : ",queue.dequeue())
print("DEQUEUE : ",queue.dequeue())