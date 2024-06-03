from task1 import *

def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def associativity(c):
    if c == '^':
        return 'R'
    return 'L'


def infix_to_postfix(s):

    result = ""
    stack = Stack()

    for c in s:

        if c == ' ':
            continue

        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            result += c

        elif c == '(':
            stack.push(c)

        elif c == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                result += stack.pop()
            stack.pop()  

        else:
            while not stack.isEmpty() and (prec(c) < prec(stack.peek()) or
                             (prec(c) == prec(stack.peek()) and associativity(c) == 'L')):
                result += stack.pop()
            stack.push(c)


    while not stack.isEmpty():
        result +=  stack.pop()

    return result


print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )")) # Output: "3 4 2 * 1 5 - / +"