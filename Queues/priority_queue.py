import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value):
        heapq.heappush(self.heap, value)
    def dequeue(self):
        return heapq.heappop(self.heap) if self.heap else "queue is empty"
    
    def display(self):
        print(self.heap)

pq = PriorityQueue()
pq.enqueue(3)
pq.enqueue(1)
pq.enqueue(2)
pq.display()
print(pq.dequeue())  # Removes 1
pq.display()

'''
Outputs:
[1, 3, 2]
1
[2, 3]
'''

'''
Time Complexity:
Enqueue: O(log N)
Dequeue: O(log N)
'''