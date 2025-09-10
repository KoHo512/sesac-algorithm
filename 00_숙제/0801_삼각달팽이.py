# 프로그래머스 68645번: 삼각 달팽이

def solution(n):
    board = [[0] * n for _ in range(n)]
    
    dx, dy = [1, 0, -1], [0, 1, -1]
    x, y = -1, 0
    d = 0
    number = 1
    
    for i in range(n, 0, -1):
        for _ in range(i):
            x, y = x + dx[d], y + dy[d]
            board[x][y] = number
            number += 1
        
        d = (d + 1) % 3
                
    return [number for line in board for number in line if number > 0]
    
#     for i in range(n):
#         number += 1
#         answer[i][0] = number
        
#     for i in range(1, n):
#         number += 1
#         answer[n - 1][i] = number
        
#     for i in range(n - 2, 0, -1):
#         number += 1
#         answer[i][i] = number
        
#     for i in range(2, n - 1):
#         number += 1
#         answer[i][1] = number
