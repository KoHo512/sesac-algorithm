# 백준 7562번: 나이트의 이동

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(x, y):
    queue = deque([(x, y, 0)])

    while queue:
        x, y, n = queue.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                if nx == fx and ny == fy:
                    return n + 1
                
                visited[nx][ny] = True
                queue.append((nx, ny, n + 1))

for _ in range(t):
    l = int(input())
    x, y = map(int, input().split())
    fx, fy = map(int, input().split())

    visited = [[False] * l for _ in range(l)]

    visited[x][y] = True
    if (x, y) == (fx, fy):
        print(0)
    else:
        print(bfs(x, y))