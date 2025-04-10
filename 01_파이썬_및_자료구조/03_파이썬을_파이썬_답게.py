## 1. List Comprehension (리스트 컴프리헨션)
numbers1 = []    # [1, 2, 3, 4, 5]

for i in range(1, 6):
    numbers1.append(i)

print(numbers1)

# [원소 | 원소에 대한 반복문]
numbers2 = [i for i in range(1, 6)]     # [1, 2, 3, 4, 5]
print(numbers2)

# [원소 | 원소에 대한 반복문 | 반복문에 대한 조건문]
numbers3 = [i for i in range(1, 6) if i % 2 == 0]   # [2, 4]
print(numbers3)



## 2. 다중 할당, 패킹, 언패킹
# 2-1. 다중 할당
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

a, b = b, a
print(a, b)     # 2 1


# 2-2. 패킹(Packing) -> 리스트로 감싼다
a, *b = 1, 2, 3, 4
print(a)    # 1
print(b)    # [2, 3, 4]

*a, b = 1, 2, 3, 4
print(a)    # [1, 2, 3]
print(b)    # 4


# 2-3. 언패킹(Unpacking) -> 감싼 걸 해제한다
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)      # 1 2 3


numbers = [1, 2, 3]

for number in numbers:
    print(number, end=" ")  # 1 2 3
print()


# * 연산자가 상황에 따라 패킹/언패킹
numbers = [1, 2, 3]
print(*numbers)     # 1 2 3



## 3. Enumerate
numbers = [8, 2, 5, 3]
# 0번째 원소: 8
# 1번째 원소: 2
# ...

for i in range(len(numbers)):
    print(f"{i}번째 원소: {numbers[i]}")

for i, number in enumerate(numbers):
    print(f"{i}번째 원소: {number}")

# 파이썬스러운 문법을 잘 알면 이렇게 한줄로 작성 가능
print(list(zip(*enumerate(numbers))))



## 4. Counter
# 4-1. 딕셔너리를 이용한 카운팅
numbers = [1, 2, 4, 1, 2, 2, 3, 2, 2]
# numbers의 원소가 각각 몇개 있는지 알고 싶다면?

counter = {}
for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)  # {1: 2, 2: 5, 4: 1, 3: 1}


# 4-2. 카운터 모듈을 이용한 카운팅
from collections import Counter

numbers = [1, 2, 4, 1, 2, 2, 3, 2, 2]
counter = Counter(numbers)

print(counter)  # Counter({2: 5, 1: 2, 4: 1, 3: 1})


common = counter.most_common()
print(common)       # [(2, 5), (1, 2), (4, 1), (3, 1)]
print(common[0])    # (2, 5)
print(common[0][0]) # 2
