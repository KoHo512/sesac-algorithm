### 이차원 리스트 기초

matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

print(matrix[0][0]) # 1
print(matrix[2][2]) # 9

matrix[2][2] = 0
print(matrix)   # [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


# 이차원 리스트의 초기화
matrix = []

for _ in range(3):
    matrix.append([0] * 4)

print(matrix)   # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

matrix = [[0] * 4 for _ in range(3)]
print(matrix)   # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# 왜 [[0] * 4] * 3 라고 하지 않을까?
matrix = [[0] * 4] * 3  # 얕은 복사
matrix[0][0] = 1
print(matrix)   # [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
# ⇒ 얕은 복사라 같은 배열이 3개 들어가는 것과 같기 때문!

# 그렇다면 [0] * 4 는 왜 가능한가?
# ⇒ mutable과 immutable의 차이!