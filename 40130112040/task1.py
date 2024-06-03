class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0


    def push(self,value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.size < 1:
            print("Stack Overflow")
            return -1
        
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value
    
    def peek(self):
        return self.head.data
    
    def isEmpty(self):
        if self.size > 0:
            return False
        else:
            return True
        
    def size(self):
        return self.size
    
    def get_max(self):
        if self.size < 1:
            print("Stack Empty")
            return -1
        p = self.head
        max = self.head.data
        while p != None:
            if p.data > max:
                max = p.data
            p = p.next
        return max


    

# stack = Stack()
# stack.push(100)
# stack.push(10)
# stack.push(20)
# print(stack.get_max()) # output: 100
# print(stack.peek()) # Output: 20
# print(stack.pop()) # Output: 20
# print(stack.isEmpty()) # Output: False