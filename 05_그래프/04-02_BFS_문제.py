### BFS 관련 문제

## 데일리알고 28번: 그래프 탐색
from collections import deque

def solution(n, edges):
    graph = [[] for _ in range(n + 1)]

    for edge in edges:
        v1, v2 = edge
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (n + 1)

    def bfs(node):
        queue = deque([node])

        while queue:
            node = queue.popleft()

            for next in graph[node]:
                if not visited[next]:
                    visited[next] = True
                    queue.append(next)

    visited[1] = True
    bfs(1)

    return sum(visited)
