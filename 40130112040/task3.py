from task1 import *



def evaluate_postfix(s):

    stack = Stack()

    for c in s:

        if c == " ":
            continue

        if c.isdigit():
            stack.push(int(c))
        else:

            if c == '+':
                num = stack.pop() + stack.pop()
                stack.push(num)
            elif c == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                num = num1 - num2 
                stack.push(num)
            elif c == '*':
                num = stack.pop() * stack.pop()
                stack.push(num)
            else :
                num2 = stack.pop()
                num1 = stack.pop()
                num = num1 / num2 
                stack.push(num)
    
    return stack.pop()


print(evaluate_postfix("3 4 + 2 * 7 /")) # Output: 2