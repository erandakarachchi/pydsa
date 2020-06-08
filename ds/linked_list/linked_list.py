class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self,head=None):
        self.head = head
        if self.head != None:
            self.size = 1
        else:
            self.size =0


    def insert_head(self,node):
        node.next = self.head
        self.head = node
        self.size +=1


    def get_head(self):
        return self.head.value


    def remove_head(self):
        self.head = self.head.next

    def show_linked_list(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.value,end="|->")
            curr_node = curr_node.next
        print("\n")

    def insert_node_to_position(self,node,position):
        #assumes that starting node (head node) is the 0th position.
        if position == 0:
            self.insert_head(node)
        elif position<=self.size:
            curr_node = self.head
            curr_pos = 0
            while curr_node != None:
                if (position-1) == curr_pos:
                    node.next = curr_node.next
                    curr_node.next = node
                    self.size +=1
                    break
                curr_node = curr_node.next
                curr_pos +=1
        else:
            return

    def remove_node_from_position(self,position):
        if position ==0:
            self.remove_head()
        else:
            curr_node = self.head
            prev_node = curr_node
            curr_position = 0
            while curr_node != None:
                print(curr_position-1,position)
                if curr_position==position:
                    break
                prev_node = curr_node
                curr_node = curr_node.next
                curr_position +=1
            prev_node.next = curr_node.next


    def insert_node_to_end(self,node):
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        #curr_node.next == None , means that it is the tail node of the linked list.
        node.next = None
        curr_node.next = node

    def get_size(self):
        return self.size



#as we need to run app from terminal.
if __name__ != "main":

    initial_node = Node(20)

    linked_list = LinkedList(initial_node)

    new_head_node = Node(30)

    linked_list.insert_head(new_head_node)

    new_node = Node(90)

    linked_list.insert_node_to_position(new_node, 0)

    print("SIZE : ",linked_list.get_size())

    linked_list.remove_head()

    new_tail_node = Node(99)

    linked_list.insert_node_to_end(new_tail_node)

    print("HEAD : ",linked_list.get_head())

    linked_list.show_linked_list()

    linked_list.remove_node_from_position(1)

    linked_list.show_linked_list()
