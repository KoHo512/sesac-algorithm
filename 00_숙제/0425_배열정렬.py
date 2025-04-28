# 데일리알고 79번: 배열 정렬

def solution(numbers):
    return sorted(numbers, key=lambda num: (num[0], abs(num[1])))
