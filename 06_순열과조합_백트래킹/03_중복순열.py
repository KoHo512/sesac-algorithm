### 중복순열 (Product)
"""
[1, 1, 1]
[1, 1, 2]
[1, 1, 3]
[1, 1, 4]
[1, 2, 1]
[1, 2, 2]
[1, 2, 3]
[1, 2, 4]
[1, 3, 1]
[1, 3, 2]
[1, 3, 3]
[1, 3, 4]
[1, 4, 1]
[1, 4, 2]
[1, 4, 3]
[1, 4, 4]
[2, 1, 1]
[2, 1, 2]
[2, 1, 3]
[2, 1, 4]
[2, 2, 1]
[2, 2, 2]
[2, 2, 3]
[2, 2, 4]
[2, 3, 1]
[2, 3, 2]
[2, 3, 3]
[2, 3, 4]
[2, 4, 1]
[2, 4, 2]
[2, 4, 3]
[2, 4, 4]
[3, 1, 1]
[3, 1, 2]
[3, 1, 3]
[3, 1, 4]
[3, 2, 1]
[3, 2, 2]
[3, 2, 3]
[3, 2, 4]
[3, 3, 1]
[3, 3, 2]
[3, 3, 3]
[3, 3, 4]
[3, 4, 1]
[3, 4, 2]
[3, 4, 3]
[3, 4, 4]
[4, 1, 1]
[4, 1, 2]
[4, 1, 3]
[4, 1, 4]
[4, 2, 1]
[4, 2, 2]
[4, 2, 3]
[4, 2, 4]
[4, 3, 1]
[4, 3, 2]
[4, 3, 3]
[4, 3, 4]
[4, 4, 1]
[4, 4, 2]
[4, 4, 3]
[4, 4, 4]
"""


## 1. 재귀
def product(current):
    # 1. 종료 조건
    if len(current) == length:
        result.append(current[:])
        return
    
    # 2. 재귀식
    # for i in range(len(numbers)): 
    # ⇒ visited 때문에 index가 필요했는데 이제 필요 x

    for number in numbers:
        current.append(number)
        product(current)
        current.pop()

numbers = [1, 2, 3, 4]
length = 3
result = []

product([])

for line in result:
    print(line)


## 2. 모듈
from itertools import product

numbers = [1, 2, 3, 4]
length = 3

for current in product(numbers, repeat=length):
    print(current)  # 튜플로 출력됨