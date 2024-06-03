from task1 import *

def sort_stack(stack: Stack):

    temp_stack = Stack()
    while not stack.isEmpty():
         
        temp = stack.pop()
 

        while not temp_stack.isEmpty() and int(temp_stack.head.data) < int(temp):
             
            stack.push(temp_stack.pop())
 

        temp_stack.push(temp)
     
    return temp_stack


stack = Stack()
stack.push(3)
stack.push(1)
stack.push(4)
sorted_stack = sort_stack(stack)
print(sorted_stack.pop()) # Output: 1
print(sorted_stack.pop()) # Output: 3