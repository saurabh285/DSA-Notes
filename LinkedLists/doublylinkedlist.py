class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, data):
        new_node = DNode(data)
        if self.head:
            new_node.next = self.head
            self.prev = new_node
        self.head = new_node
    
    def insert_at_tail(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    
    def delete_node(self, val):
        temp = self.head
        while temp and temp.data!=val:
            temp= temp.next
        if not temp: 
            return
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        if temp == self.head:
            self.head = temp.next
    
    def insert_at_position(self, data, position):
        new_node = DNode(data)
        if position == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        temp = self.head
        for _ in range(position-2):
            if temp is None:
                raise IndexError("Position out of bounds")
            temp = temp.next

        new_node.prev = temp
        new_node.next = temp.next
        
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
    
    def delete_at_position(self, position):
        if not self.head:
           return

        temp = self.head
        if position == 1:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None
            return
        
        for _ in range(position - 1):
            temp = temp.next
            if temp is None:
                raise IndexError("Position out of bounds")
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
            temp = None

    def display(self):
        """Prints the linked list"""
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
dll.insert_at_head(2)
dll.insert_at_tail(4)
dll.display()
dll.delete_node(2)
dll.display()
dll.delete_node(4)
dll.display()
dll.insert_at_position(1, 1)
dll.insert_at_position(2, 2)
dll.insert_at_position(3, 2)  # Insert at position 2
dll.display()
dll.delete_node(1)
dll.delete_node(2)
dll.delete_node(3)
dll.display()
dll.head = DNode(1)
dll.head.next = DNode(2)
dll.head.next.prev = dll.head
dll.head.next.next = DNode(3)
dll.head.next.next.prev = dll.head.next

dll.display()
dll.delete_at_position(2)  # Delete node at position 2
dll.display()


'''
Outputs:
2 <-> 4 <-> None
4 <-> None
None
1 <-> 3 <-> 2 <-> None
None
1 <-> 2 <-> 3 <-> None
1 <-> 3 <-> None
'''


'''
Time Complexity:
Insertion at head/tail: O(1)
Deletion: O(N)
Traversal: O(N)
'''