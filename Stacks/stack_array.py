class StackArray:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if len(self.stack)!=0:
            return self.stack.pop()
        return "Stack Empty"
    
    def peek(self):
        return self.stack[-1] if len(self.stack)!=0 else "Stack Empty"
    
    def display(self):
        print(self.stack)

s = StackArray()
s.push(10)
s.push(20)
s.push(30)
s.display()
print(s.pop())  # Removes 30
s.display()

'''
Outputs:
[10, 20, 30]
30
[10, 20]
'''

'''
Time Complexity:
Push: O(1)
Pop: O(1)
Peek: O(1)
'''