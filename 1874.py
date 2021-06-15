from collections import deque

n = int(input())

oriStack = deque([])

for i in range(n, 0, -1):
    oriStack.append(i)

print(oriStack.pop())
