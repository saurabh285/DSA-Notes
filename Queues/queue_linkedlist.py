# python queue_linkedlist.py
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, val):
        new_node = Node(val)

        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return "Queue empty"
        temp = self.front
        self.front = temp.next
        if not self.front:
            self.rear = None
        return temp.value
    
    def display(self):
        temp = self.front
        while temp:
            print(temp.value, end = " -> ")
            temp = temp.next
        print("None")

ql = QueueLinkedList()
ql.enqueue(10)
ql.enqueue(20)
ql.enqueue(30)
ql.display()
print(ql.dequeue())  # Removes 10
ql.display()

'''
Outputs:
10 -> 20 -> 30 -> None
10
20 -> 30 -> None
'''

'''
Time Complexity: 
Enqueue: O(1)
Dequeue: O(1)
'''