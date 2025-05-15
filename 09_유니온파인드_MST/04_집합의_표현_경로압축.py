# 백준 1717번: 집합의 표현
# 경로 압축

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find(x):
    # # 1. 종료 조건
    # if x == parent[x]:
    #     return x
    
    # # 2. 재귀식
    # parent[x] = find(parent[x])
    # return parent[x]

    if x != parent[x]:
        parent[x] = find(parent[x])  # path compression

    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return
    
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

n, m = map(int, input().split())
parent = list(range(n + 1))

for _ in range(m):
    command, x, y = map(int, input().split())

    if command == 0:
        union(x, y)
    else:
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")

# ⇒ 합집합하는 과정에서
