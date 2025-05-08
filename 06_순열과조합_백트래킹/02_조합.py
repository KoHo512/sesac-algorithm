### 조합 (Combinations)
## 순서가 "없게" 뽑는 경우의 수
"""
[1, 2, 3]
[1, 2, 4]
[1, 3, 4]
[2, 3, 4]
"""

## 1. 재귀
def combinations(current, start):
    # 1. 종료 조건
    if len(current) == length:
        result.append(current[:])
        return
    
    # 2. 재귀식
    for i in range(start, len(numbers)):
        current.append(numbers[i])
        combinations(current, i + 1)
        current.pop()

numbers = [1, 2, 3, 4]
length = 3
result = []

combinations([], 0)

for line in result:
    print(line)


## 문제 풀기
# 데일리알고 100번: 조합
def solution(n, m):
    def combinations(current, start):
        # 1. 종료 조건
        if len(current) == m:
            result.append(current[:])
            return
        
        # 2. 재귀식
        for i in range(start, n + 1):
            current.append(i)
            combinations(current, i + 1)
            current.pop()

    result = []
    combinations([], 1)

    return result


# 백준 6603번: 로또 (⇒ 02-02_조합_문제.py)