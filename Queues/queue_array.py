class QueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return "Empty Queue"
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)

q = QueueArray()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.dequeue())  
q.display()

'''
Outputs:
[10, 20, 30]
10
[20, 30]
'''

'''
Time Complexity:
Enqueue: O(1)
Dequeue: O(N) (since pop(0) shifts elements)
'''