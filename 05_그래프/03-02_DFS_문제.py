### DFS 관련 문제

## 데일리알고 28번: 그래프 탐색
def solution(n, edges):
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (n + 1)

    def dfs(node):
        for next in graph[node]:
            if not visited[next]:
                visited[next] = 1
                dfs(next)

    visited[1] = True
    dfs(1)

    return sum(visited)


## 백준 2606번: 바이러스
import sys

input = sys.stdin.readline

com_num = int(input())
line_num = int(input())

graph = [[] for _ in range(com_num + 1)]

for _ in range(line_num):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (com_num + 1)

def dfs(node):
    for next in graph[node]:
        if not visited[next]:
            visited[next] = True
            dfs(next)

visited[1] = True
dfs(1)

print(sum(visited) - 1)