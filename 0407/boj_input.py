# 입력
# 1
# 입력 코드
n = int(input())


# 입력
# a
# 입력 코드
c = input()


# 입력
# spring flower
# 입력 코드
a, b = input().split()


# 입력
# spring flower warm
# 입력 코드
a, b, c = input().split()


# 입력
# "1 2"
# 입력 코드
# [X] int(input().split())
# split()은 list 자료형 반환 => list 자료형은 int() 함수 적용 불가
# 리스트에 저장된 값 하나하나에 int() 함수 적용해야함

# map(리스트에 저장된 값에 적용할 함수, 리스트)
n1, n2 = map(int, input().split())
print(n1, n2)   # 1, 2


# 입력
# 2 3
# 1 2 3
# 4 5 6
# 입력 코드
n, m = map(int, input().split())
list_2d = []
for i in range(n):
    list_1d = list(map(int, input().split()))
    list_2d.append(list_1d)
print(list_2d)  # [[1, 2, 3], [4, 5, 6]]