### input, readline

## 1. input을 이용한 기본 문법
n = int(input())
print(n)


## 2. readline을 이용한 빠른 입력
import sys

input = sys.stdin.readline

n = int(input())
print(n)

word = list(input().rstrip())
print(word)


## 3. 한 줄 리스트 입력
import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))
print(numbers)

# 다중 할당도 가능
a, b = list(map(int, input().split()))
print(a + b)

# 다중 할당으로 받을 때는 list로 감싸지 않아도 됨
a, b = map(int, input().split())

# list 외에 다른 collection으로도 처리 가능
numbers = tuple(map(int, input().split()))
numbers = set(map(int, input().split()))


## 4. A+B - 2
import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
print(a + b)


## 5. A+B - 3
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(a + b)


## 6. A+B - 6
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split(','))
    print(a + b)
