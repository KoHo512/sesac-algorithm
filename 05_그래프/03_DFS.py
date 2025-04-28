### 깊이우선탐색 (Depth-First Search, DFS)

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

for line in graph:
    print(line)
    """
    [1, 2]
    [0, 3, 4]
    [0, 4, 5]
    [1]
    [1, 2, 6]
    [2]
    [4]
    """


## 2. 방문 리스트 (visited)
visited = [False] * n


## 3. 깊이우선탐색
# 함수 호출 = 정점 방문 = 스택 push
# 함수 종료 = 더 이상 갈 곳 x = 스택 pop
def dfs(node):
    # 현재 방문 정점 출력
    print(node)

    # 인접한 정점 중 방문하지 않은 곳으로 이동
    for next in graph[node]:
        if not visited[next]:
            visited[next] = node    # 다음 정점 방문 처리
            dfs(next)               # 실제로 다음 정점으로 이동


visited[0] = True
dfs(0)


# 아래와 같이 dfs 함수 시작 부분에서 방문 처리도 가능
# 다만, bfs에서는 위와 같이 방문 처리를 해야 해서 통일성을 위해 위와 같이 작성
def dfs(node):
    visited[node] = True
    print(node)

    for next in graph[node]:
        if not visited[next]:
            dfs(next)

dfs(0)


## 문제 풀기 (⇒ 03-02_DFS_문제.py)
# 데일리알고 28번: 그래프 탐색
# 백준 2606번: 바이러스