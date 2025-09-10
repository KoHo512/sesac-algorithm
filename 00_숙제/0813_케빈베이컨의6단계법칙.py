# 백준 1389번: 케빈 베이컨의 6단계 법칙

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u1, u2 = map(int, input().split())

    graph[u1].append(u2)
    graph[u2].append(u1)

connection = [float("INF")] * (n + 1)

for i in range(1, n + 1):
    queue = deque([i])
    
    visited = [0] * (n + 1)
    visited[i] = 1
    total = 0

    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)

    connection[i] = sum(visited) - 1

print(connection.index(min(connection)))