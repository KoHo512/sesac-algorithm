# 데일리알고 70번: 이차원 배열의 회전

def solution(numbers, rotate):
    for _ in range(rotate // 90):
        numbers = list(zip(*numbers[::-1]))

    return numbers