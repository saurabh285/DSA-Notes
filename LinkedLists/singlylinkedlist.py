class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def delete_node(self, val):
        temp = self.head
        if temp and temp.data == val:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != val:
            prev = temp
            temp = temp.next
        if temp: 
            prev.next = temp.next
    
    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        
        for _ in range(position-2):
            if temp is None:
                raise IndexError('Position out of bounds')
            temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node
    
    def delete_at_position(self, position):
        if not self.head: return

        temp = self.head
        
        if position == 1:
            self.head = temp.next
            temp = None
            return
        
        prev = None

        for _ in range(position - 1):
            prev = temp
            temp = temp.next
            if temp is None:
                raise IndexError('Position out of bounds')
        prev.next = temp.next
        temp = None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = SinglyLinkedList()
ll.insert_at_head(3)
ll.insert_at_head(2)
ll.insert_at_tail(5)
ll.display()
ll.delete_node(2)
ll.display()
ll.delete_node(3)
ll.delete_node(5)
ll.display()
ll.insert_at_position(10, 1)  # Insert 1 at position 1
ll.insert_at_position(20, 2)  # Insert 2 at position 2
ll.insert_at_position(30, 2)  # Insert 3 at position 2 (between 1 and 2)
ll.display()
ll.display()
ll.delete_at_position(2)  # Delete node at position 2
ll.display()

'''
Outputs:
2 -> 3 -> 5 -> None
3 -> 5 -> None
None
10 -> 30 -> 20 -> None
10 -> 30 -> 20 -> None
10 -> 20 -> None
'''

'''
Time Complexity:
Insertion at head: O(1)
Insertion at tail: O(N)
Deletion: O(N) (worst case)
Traversal: O(N)
'''