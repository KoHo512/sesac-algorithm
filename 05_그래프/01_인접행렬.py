### 인접 행렬
"""
0 1
0 2
0 5
0 6
3 4
3 5
4 5
4 6
"""

# 무방향 그래프
n = 7   # 정점의 개수
m = 8   # 간선의 개수

graph = [[0] * n for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

for line in graph:
    print(line)
    """
    [0, 1, 1, 0, 0, 1, 1]
    [1, 0, 0, 0, 0, 0, 0]
    [1, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 1, 1, 0]
    [0, 0, 0, 1, 0, 1, 1]
    [1, 0, 0, 1, 1, 0, 0]
    [1, 0, 0, 0, 1, 0, 0]
    """


print()


# 유방향 그래프
n = 7   # 정점의 개수
m = 8   # 간선의 개수

graph = [[0] * n for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1

for line in graph:
    print(line)
    """
    [0, 1, 1, 0, 0, 1, 1]
    [0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 1, 1, 0]
    [0, 0, 0, 0, 0, 1, 1]
    [0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0]
    """


# 하지만 공간복잡도가 높음 (공간의 낭비가 심함)
# ⇒ 인접 리스트 사용