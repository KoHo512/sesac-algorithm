### print
print("1")


## 1. 여러 인자를 넣으면 공백을 기준으로 출력
print("1", "2", "3")    # 1 2 3


## 2. 맨 끝의 개행을 다른 문자로 바꿀 수 있음 (end)
print("hello", end="$") # hello$
print("python")         # hello$python으로 붙어서 나옴
                        # end="\n"이 생략되어있는 것


## 3. 구분자를 다른 문자로 바꿀 수 있음 (sep)
print("1", "2", "3", sep="$")   # 1$2$3
print("1", "2", "3", sep="\n")


## 4. f-string
name = "KoHo"
print("안녕하세요! " + name)    # 안녕하세요! KoHo
print(f"안녕하세요! {name}")    # 안녕하세요! KoHo

age = 40
print(f"안녕하세요! {name}, 나이는 {age - 10}입니다.")  # 안녕하세요! KoHo, 나이는 30입니다.


## 5. A+B - 7
import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    a, b = map(int, input().split())
    print(f"Case #{t}: {a + b}")


## 6. A+B - 8
import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    a, b = map(int, input().split())
    print(f"Case #{t}: {a} + {b} = {a + b}")