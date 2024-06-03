from task1 import *


def longest_valid_parentheses(s):
    stack = Stack()
    stack.push(-1)
    max_length = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.push(i)
        else:
            stack.pop()
            if stack.isEmpty():
                stack.push(i)
            else:
                max_length = max(max_length, i - stack.peek())

    return max_length


print(longest_valid_parentheses("(()"))  # Output: 2
print(longest_valid_parentheses(")()())"))  # Output: 4