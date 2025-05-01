# 백준 1260번: DFS와 BFS

import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for line in graph:
    line.sort()

# DFS 탐색
route = []
visited = [False] * (n + 1)

def dfs(node):
    for next in graph[node]:
        if not visited[next]:
            visited[next] = True
            route.append(next)
            dfs(next)

visited[v] = True
route.append(v)
dfs(v)

print(*route)

# BFS 탐색
route = []
visited = [False] * (n + 1)

def bfs(node):
    queue = deque([node])

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                route.append(next)
                queue.append(next)

visited[v] = True
route.append(v)
bfs(v)

print(*route)