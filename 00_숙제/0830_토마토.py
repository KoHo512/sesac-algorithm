# 백준 7576번: 토마토

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

box = []

for _ in range(n):
    box.append(list(map(int, input().split())))

queue = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j, 0))

while queue:
    x, y, day = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = 1
            queue.append((nx, ny, day + 1))

if any(0 in line for line in box):
    print(-1)
else:
    print(day)