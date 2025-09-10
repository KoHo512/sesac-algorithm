# 백준 2468번: 안전 영역

import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and field[nx][ny] > h:
                visited[nx][ny] = True
                queue.append((nx, ny))

n = int(input())
field = []

for _ in range(n):
    field.append(list(map(int, input().split())))

max_h = max([max(line) for line in field])
max_sa = 0

for h in range(0, max_h):
    total = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if field[i][j] > h and not visited[i][j]:
                total += 1
                visited[i][j] = True
                bfs(i, j)

    max_sa = max(max_sa, total)

print(max_sa)