# 백준 10773번: 제로

import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
queue = deque()

for _ in range(k):
    n = int(input())

    if n == 0:
        queue.pop()
    else:
        queue.append(n)

print(sum(queue))