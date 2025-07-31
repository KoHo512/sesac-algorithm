# 백준 9291번: 스도쿠 채점

import sys

input = sys.stdin.readline

n = int(input())

def check_1to9(lst):
    return sorted(lst) == list(range(1, 10))


def check_correct(sudoku):
    for i in range(9):
        if not check_1to9(sudoku[i]):
            return "INCORRECT"
        
        if not check_1to9(list(sudoku[j][i] for j in range(9))):
            return "INCORRECT"
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_1to9(list(sudoku[x][y] for x in range(i, i + 3) for y in range(j, j + 3))):
                return "INCORRECT"
        
    return "CORRECT"


for t in range(1, n + 1):
    if t > 1:
        input()

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print(f"Case {t}: {check_correct(sudoku)}")
