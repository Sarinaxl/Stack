from task1 import *

def is_balanced(expression):
    stack = Stack()
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.isEmpty() or stack.peek() != bracket_pairs[char]:
                return False
            stack.pop()

    return stack.size == 0



print(is_balanced("{[()]}")) # Output: True
print(is_balanced("({[)")) # Output: False