# 백준 3190번: 뱀

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
apples = set()

for _ in range(k):
    r, c = map(int, input().split())
    apples.add((r - 1, c - 1))

l = int(input())
directions = {}

for _ in range(l):
    s, direction = input().split()
    s = int(s)
    directions[s] = direction

x = y = d = t = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 우하좌상
queue = deque([(x, y)])

while True:
    t += 1
    nx, ny = x + dx[d], y + dy[d]

    if not (0 <= nx < n and 0 <= ny < n) or (nx, ny) in queue:
        print(t)
        break

    queue.append((nx, ny))
    x, y = nx, ny

    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        queue.popleft()
            

    if t in directions:
        if directions[t] == "D":
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4