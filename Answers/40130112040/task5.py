from task1 import *

def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False

def prefix_to_postfix(s):

    s = s[::-1]

    stack = Stack()

 
    for c in s:

        if c == ' ':
            continue
 
        if (isOperator(c)):

            op1 = stack.pop()
            op2 = stack.pop()
 
            temp = op1 + op2 + c
 
            stack.push(temp)
 
        else:
 
            stack.push(c)
 
    
    return stack.pop()


print(prefix_to_postfix("* + 3 4 2")) # Output: "3 4 + 2 *"