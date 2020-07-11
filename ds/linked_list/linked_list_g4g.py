class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class LinkedList:
    def __init__(self,head=None):
        self.head = head
        self.tail = head
        
    def insertToHead(self,value):
        newHeadNode = Node(value)
        newHeadNode.next = self.head
        self.head = newHeadNode
    
    def insertToEnd(self,value):
        newTailNode = Node(value)
        self.tail.next = newTailNode
        self.tail = newTailNode
        
    def removeHead(self):
        self.head = self.head.next
        
    def removeTail(self):
        current = self.head
        prev = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        self.tail = prev
        
    def showLinkedList(self):
        current = self.head
        while current:
            print(current.data, end = "->")
            current = current.next
        print("\n")
            
            
headNode = Node(30)
llist = LinkedList(headNode)
llist.insertToHead(50)
llist.insertToEnd(99)
llist.insertToHead(54)
llist.insertToEnd(76)
llist.insertToHead(120)

print("CREATED LIST")
llist.showLinkedList()

print("REMOVE HEAD")
llist.removeHead()
llist.showLinkedList()

print("REMOVE TAIL")
llist.removeTail()
llist.showLinkedList()