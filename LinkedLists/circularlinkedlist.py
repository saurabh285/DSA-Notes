class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next!=self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    def display(self):
        if not self.head: return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")

cll = CircularLinkedList()
cll.insert(1)
cll.insert(2)
cll.insert(3)
cll.display()

'''
Outputs:
1 -> 2 -> 3 -> (Back to head)
'''

'''
Time Complexity:
Insertion: O(N)
Traversal: O(N)
'''