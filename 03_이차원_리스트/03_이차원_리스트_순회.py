### 이차원 리스트 순회


## 1. 행 우선 순회 (행순회)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

"""
다음과 같이 출력하려면?
1 2 3 4
5 6 7 8
9 0 1 2
"""
for i in range(3):      # 행
    for j in range(4):  # 열
        print(matrix[i][j], end=" ")
    print()



## 2. 열 우선 순회 (열순회)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

"""
다음과 같이 출력하려면?
1 5 9
2 6 0
3 7 1
4 8 2
"""
for j in range(4):      # 열
    for i in range(3):  # 행
        print(matrix[i][j], end=" ")
    print()



## 3. 이차원 리스트의 총합
matrix = [
    [0, 5, 3, 1],
    [4, 6, 10, 8],
    [9, -1, 1, 5]
]

total = 0

for i in range(3):
    for j in range(4):
        total += matrix[i][j]

print(total)    # 51


# 내장함수 sum 이용
total = 0

# for i in range(3):
#     total += sum(matrix[i])

for line in matrix:
    total += sum(line)

print(total)    # 51



## 이차원 배열의 최소와 최대
def solution(numbers):
    n = len(numbers)    # 행
    m = len(numbers[0]) # 열
    min_number = numbers[0][0]
    max_number = numbers[0][0]

    # 행순회
    for i in range(n):
        for j in range(m):
            number = numbers[i][j]

            if number < min_number:
                min_number = number
            elif number > max_number:
                max_number = number
    
    return [min_number, max_number]