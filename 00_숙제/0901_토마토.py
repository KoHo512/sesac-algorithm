# 백준 7569번: 토마토

import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

box = [[] for _ in range(h)]
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
queue = deque()

for k in range(h):
    for j in range(n):
        line = list(map(int, input().rsplit()))
        box[k].append(line)

        for i in range(m):
            if line[i] == 1:
                queue.append((i, j, k, 0))

max_days = 0

while queue:
    x, y, z, days = queue.popleft()
    max_days = max(max_days, days)

    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = 1
            queue.append((nx, ny, nz, days + 1))

for k in range(h):
    for j in range(n):
        for i in range(m):
            if box[k][j][i] == 0:
                max_days = -1

print(max_days)