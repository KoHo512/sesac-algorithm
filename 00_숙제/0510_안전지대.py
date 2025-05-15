# 프로그래머스 120866번: 안전지대

def solution(board):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    n = len(board)
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                        board[nx][ny] = 2
                        
    return sum([line.count(0) for line in board])
