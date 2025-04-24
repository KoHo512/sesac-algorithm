### 인접 리스트
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

graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for line in graph:
    print(line)
    """
    [1, 2, 5, 6]
    [0]
    [0]
    [4, 5]
    [3, 5, 6]
    [0, 3, 4]
    [0, 4]
    """


print()


# 유방향 그래프
n = 7   # 정점의 개수
m = 8   # 간선의 개수

graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

for line in graph:
    print(line)
    """
    [1, 2, 5, 6]
    []
    []
    [4, 5]
    [5, 6]
    []
    []
    """


## 숙제
# 프로그래머스 81302번: 거리두기 확인하기
# 그냥 델타 탐색을 하려면 
# [상하좌우 좌상 우상 좌하 우하 상상 하하 좌좌 우우]에 대한
# 경우의 수 12개를 모두 확인해야 함

# 전체 자리를 순회하면서 P(응시자)라면
# 상하좌우 델타 탐색을 하면서
# 0(빈 테이블)이라면 다른 문자열로 변경
# 이후 탐색에서 P에서 델타 탐색을 했을 때
# 변경한 문자열이 있다면? 거리두기 실패


## 풀이
# 백준 2563번: 색종이