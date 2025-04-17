# 백준 2738번: 행렬 덧셈

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] += matrix2[i][j]

# for i in range(n):
#     print(*matrix[i])

for line in matrix:
    print(*line)

# ----------

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        matrix[i][j] += line[j]

for i in range(n):
    print(*matrix[i])