### 사용자 입력과 출력

# ## 파이썬 입력
# # input() 함수
# number1 = input()

# # 주의: 모든 입력 함수는 문자열(String)로 입력됨
# # type(값): 값의 자료형을 반환하는 함수
# print(type(number1))    # <class 'str'>

# # 숫자형이 필요하면 형 변환
# number2 = int(number1)
# print(type(number2))    # <class 'int'>


# # 백준 문제 풀이용 빠른 입력 방법 코드
# import sys

# # input()   # 느림
# # sys.stdin.readline()    # 빠름

# # input()     # 기존의 input()이 아니라, sys.stdin.readline()로 대치

# # sys.stdin.readline()의 문제점
# # - 개행 문자(\n)가 같이 입력됨
# # - 일반적으로 입력값 양쪽 공백을 지워서(strip) 사용
# number = sys.stdin.readline().strip()


## 파이썬 출력
# print() 함수의 end 인자
# 출력 문자열의 마지막 문자열을 결정하는 인자
# 기본값은 개행문자(\n)
print("a", end="\n")    # 기본값
print("a", end="+++")