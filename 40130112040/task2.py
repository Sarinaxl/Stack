from task1 import *

def reverse_string(s):
    
    stack = Stack()
    for c in s:
        stack.push(c)
    
    new_s = ""

    while not stack.isEmpty():
        new_s += stack.pop()

    return new_s


print(reverse_string("hello")) # Output: "olleh"