### 너비우선탐색 (Breadth-First Search, BFS)

## 1. 그래프 구현 (인접리스트)
"""
7 7
0 1
0 2
1 3
1 4
2 4
2 5
4 6
"""
n, m = map(int, input().split())    # 정점, 간선 개수
graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


## 2. 방문 리스트 (visited)
visited = [False] * n


## 3. 너비우선탐색
from collections import deque

def bfs(node):
    queue = deque([node])   # 큐에 출발 정점을 넣고 시작

    # 큐가 비어있지 않으면 탐색을 지속하고,
    # 큐가 비면 탐색을 종료
    while queue:
        # 큐에서 popleft는 해당 정점을 방문한다는 의미
        node = queue.popleft()

        for next in graph[node]:
            if not visited[next]:
                visited[next] = True    # 이동할 정점 방문 처리
                queue.append(next)      # 이동할 정점 큐에 삽입

visited[0] = True
bfs(0)


## 문제 풀기 (⇒ 04-02_BFS_문제.py)
# 데일리알고 28번: 그래프 탐색