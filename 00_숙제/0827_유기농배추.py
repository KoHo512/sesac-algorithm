# 백준 1012번: 유기농 배추

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        v1, v2 = map(int, input().split())
        graph[v2][v1] = 1
    
    total = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                total += 1
                dfs(i, j)
    
    print(total)