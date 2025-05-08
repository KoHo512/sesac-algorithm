### 순열 (Permutation)
## 순서가 "있게" 뽑는 경우의 수
"""
[1, 2, 3]
[1, 2, 4]
[1, 3, 2]
[1, 3, 4]
[1, 4, 2]
[1, 4, 3]
[2, 1, 3]
[2, 1, 4]
[2, 3, 1]
[2, 3, 4]
[2, 4, 1]
[2, 4, 3]
[3, 1, 2]
[3, 1, 4]
[3, 2, 1]
[3, 2, 4]
[3, 4, 1]
[3, 4, 2]
[4, 1, 2]
[4, 1, 3]
[4, 2, 1]
[4, 2, 3]
[4, 3, 1]
[4, 3, 2]
"""


## 1. 반복문
numbers = [1, 2, 3, 4]
result = []

for i in range(len(numbers)):
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            if i != j and j != k and k != i:
                result.append([numbers[i], numbers[j], numbers[k]])

for line in result:
    print(line)


## 2. 재귀
def permutations(current):
    # 1. 종료 조건
    if len(current) == length:
        # result.append(current)    # 얕은 복사
        result.append(current[:])
        return
    
    # 2. 점화식(재귀식)
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            current.append(numbers[i])

            permutations(current)

            visited[i] = False
            current.pop()


numbers = [1, 2, 3, 4]
length = 3  # 뽑고 싶은 갯수
visited = [False] * len(numbers)
result = []

permutations([])

for line in result:
    print(line)


## 3. 모듈(라이브러리)
from itertools import permutations

numbers = [1, 2, 3, 4]
length = 3

for current in permutations(numbers, length):
    print(current)  # 튜플로 출력됨


## 문제 풀기
# 데일리알고 99번: 순열
def solution(n, m):
    def permutations(current):
        # 1. 종료조건
        if len(current) == m:
            result.append(current[:])
            return
        
        # 2. 재귀식
        for number in range(1, n + 1):
            if not visited[number]:
                visited[number] = True
                current.append(number)

                permutations(current)

                visited[number] = False
                current.pop()

    result = []
    visited = [False] * (n + 1)

    permutations([])

    return result