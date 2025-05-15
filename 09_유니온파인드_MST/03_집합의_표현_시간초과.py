# 백준 1717번: 집합의 표현

import sys

input = sys.stdin.readline

def find(x):
    while x != parent[x]:
        x = parent[x]

    return x

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

# ⇒ 기존 방식으로 풀면 시간 초과 발생
