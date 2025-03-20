class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.top: return "Stack empty"

        popped = self.top.value
        self.top = self.top.next
        return popped
    
    def peek(self):
        return self.top.value if self.top else "Stack empty"
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
        temp = self.top
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
sll = StackLinkedList()
sll.push(10)
sll.push(20)
sll.push(30)
sll.display()
print(sll.pop())  
sll.display()

'''
Outputs:
30 -> 20 -> 10 -> None
30
20 -> 10 -> None
'''

'''
Time Complexity:
Push: O(1)
Pop: O(1)
'''