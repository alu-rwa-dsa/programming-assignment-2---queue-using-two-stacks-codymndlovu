# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# helper function
def fillstack(stack1, stack2):
    """Fills stack2 using stack1.
    
    Removes each element in stack1 
    and pushes it to stack2.
    """
    while stack1.top:
        stack2.push(stack1.pop())

class Stack:
    def __init__(self):
        self.top = None
        self.items = []
        
    def isempty(self):
        return self.top == None
        
    def push(self, item):
        self.top = item
        self.items.append(item)
        
    def pop(self):
        if self.isempty():
            return None
        
        item = self.items.pop()
        if len(self.items) == 0:
            self.top = None
        else:
            self.top = self.items[-1]
        return item
    
    def peek(self):
        return self.top
    
    
    
class Queue:
    def __init__(self):
        self.head = None
        self.enq_stack = Stack()
        self.deq_stack = Stack()
        
    def enqueue(self, element):
        if not self.head:
            self.head = element
        self.enq_stack.push(element)
        
    def dequeue(self):
        if self.deq_stack.isempty():
            fillstack(self.enq_stack, self.deq_stack)

        element = self.deq_stack.pop()

        if self.deq_stack.isempty():
            fillstack(self.enq_stack, self.deq_stack)

        self.head = self.deq_stack.top
        return element
    
if __name__ == '__main__':
    queue = Queue()
    n = int(input())
    
    for _ in range(n):
        args = list(map(int, input().rstrip().split()))
        type_ = args[0]
        
        if type_ == 1:
            queue.enqueue(args[1])
        elif type_ == 2:
            queue.dequeue()
        elif type_ == 3:
            print(queue.head, file = sys.stdout)
