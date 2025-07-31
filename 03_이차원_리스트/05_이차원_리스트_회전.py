### 이차원 리스트 회전

## 시계 방향 90도 회전 (오른쪽으로 회전)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

n = 3
m = 4

# 1. 행과 열의 크기를 바꾼 새로운 이차원 리스트를 초기화
# 이차원 리스트 초기화 = 모든 원소를 0으로 만듦

# rotated_matrix = []
# for _ in range(m):
#     line = [0] * n
#     rotated_matrix.append(line)
# print(rotated_matrix)   # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

rotated_matrix = [[0] * n for _ in range(m)]


# 2. 반복문을 돌면서 새로운 이차원 리스트 채우기
for i in range(m):
    for j in range(n):
        rotated_matrix[i][j] = matrix[n - 1 - j][i]
        """
        n - 1 - j: 행을 거꾸로
        i: 열
        """

print(rotated_matrix)   # [[9, 5, 1], [0, 6, 2], [1, 7, 3], [2, 8, 4]]

for line in rotated_matrix:
    print(line)
    """
    [9, 5, 1]
    [0, 6, 2]
    [1, 7, 3]
    [2, 8, 4]
    """

# ----------

## 내장함수 zip을 이용한 회전
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]


# 일단 zip에 대해 알아보자
a = zip([1, 2], [3, 4], [5, 6])
print(a)    # <zip object at 0x000001D1A49AEEC0>

a = list(zip([1, 2], [3, 4], [5, 6]))
print(a)    # [(1, 3, 5), (2, 4, 6)]

# ⇒ zip은 여러 종류의 콘텐츠들을, 같은 index끼리 튜플로 묶어줌


# 이제 zip을 이용해서 회전해보자
print(list(zip(matrix)))    # [([1, 2, 3, 4],), ([5, 6, 7, 8],), ([9, 0, 1, 2],)]
# ⇒ 리스트를 풀어서 넣어줘야함

print(list(zip(*matrix)))   # [(1, 5, 9), (2, 6, 0), (3, 7, 1), (4, 8, 2)]
# ⇒ 순서가 역순이어야 함

print(list(zip(*matrix[::-1])))     # [(9, 5, 1), (0, 6, 2), (1, 7, 3), (2, 8, 4)]

rotated_matrix = list(zip(*matrix[::-1]))
for line in rotated_matrix:
    print(line)
    """
    (9, 5, 1)
    (0, 6, 2)
    (1, 7, 3)
    (2, 8, 4)
    """
# ⇒ 튜플을 리스트로 변환

rotated_matrix = list(map(list, zip(*matrix[::-1])))
print(rotated_matrix)   # [[9, 5, 1], [0, 6, 2], [1, 7, 3], [2, 8, 4]]