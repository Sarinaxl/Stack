from task1 import *

def daily_temperatures(temperatures):

    stack = Stack()

    result = [0] * len(temperatures)
    
    for i, temp in enumerate(temperatures):

        while not stack.isEmpty() and temp > temperatures[stack.peek()]:

            prev_index = stack.pop()

            result[prev_index] = i - prev_index
        

        stack.push(i)
    
    return result


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])) # Output: [1, 1, 4, 2, 1, 1, 0, 0]
