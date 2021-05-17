stack = []

stack.append('A')
stack.append('B')
stack.append('C')

print('Initial Stack: ', stack)

print('Elements poped from Stack: ')
print(stack.pop())
print(stack.append('1'))
print(stack.append('2'))
print(stack.pop())

print('Final Stack: ', stack)

from collections import deque
stack =  deque()
print(dir(stack))               #It will give all the methods used in Stack.
