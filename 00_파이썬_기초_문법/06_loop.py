### 반복문(Loop)

## for 반복문
# 자바
"""
int[] arr = new int[]{1, 2, 3, 4, 5}
for (int i = 0; i < arr.lenght; i++) {
    코드
}
"""

# 자바 향상된 loop문
"""
for(int n: arr) {
    코드
}
"""

# 파이썬
list_ = [1, 2, 3, 4, 5] # 컬렉션
"""
for 반복문 내 변수 in 컬렉션:
    들여쓰기로 구분한 코드 블럭
"""
for number in list_:
    print(number)
    """
    1
    2
    3
    4
    5
    """


# N번만큼 반복하고 싶을 때
N = 10

# 자바
"""
for (int i = 0; i < N; i++) {
    반복할 코드
}
"""

# 파이썬
for i in range(0, N, 1):
    print(i)
    """
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    """


# for ~ else 문
# while ~ else 문
"""
for 변수 in 컬렉션:
    코드
else:
    코드
"""
"""
while 반복 조건식:
    코드
else:
    코드
"""

list_ = [1, 3, 5, 7, 9]
for number in list_:
    # number가 짝수면 반복문 종료
    if number % 2 == 0:
        break
else:
    # 반복문이 break에 의해 종료되지 않으면 실행
    # break에 의해 종료되면 실행 X
    print("리스트에 짝수가 없음")


### 2차원 리스트
# 자바
"""
for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
        코드
    }
}
"""

# 파이썬
"""
for i in range(0, 10, 1):
    for j in range(0, 10, 1):
        코드
"""

list_2d = [[]]              # 1x0 2차원 리스트
list_2d = [[], [], []]      # 3x0 2차원 리스트
list_2d = [[1], [2], [3]]   # 3x1 2차원 리스트
list_2d = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
] # 3x3 2차원 리스트

# 내부 리스트의 수 => 세로, 행, row, r, y
# 내부 리스트가 가진 값의 수 => 가로, 열, col, c, x

print(list_2d[1][0])    # 4

y = 1
x = 0
print(list_2d[y][x])    # 4
# 많은 문서에서 [y][x], [r][c]으로 작성함

list_2d[1][2] = -6
print(list_2d)  # [[1, 2, 3], [4, 5, -6], [7, 8, 9]]


## 2차원 배열 순회
# 세로 길이
row = len(list_2d)

# 가로 길이
col = len(list_2d[0])

for y in range(0, row, 1):
    for x in range(0, col, 1):
        print(list_2d[y][x])
        """
        1
        2
        3
        4
        5
        -6
        7
        8
        9
        """