# 프로그래머스 64061번: 크레인 인형뽑기 게임

from collections import deque

def solution(board, moves):
    m, n = len(board[0]), len(board)
    
    queue = [deque() for _ in range(m)]
    basket = deque()
    answer = 0
    
    for x in range(m):
        for y in range(n-1, -1, -1):
            if board[y][x] > 0:
                queue[x].append(board[y][x])
    
    for move in moves:
        if queue[move - 1]:
            basket.append(queue[move - 1].pop())
        
            if len(basket) >= 2 and basket[-1] == basket[-2]:
                answer += 2
                basket.pop()
                basket.pop()
    
    return answer

# ----------

from collections import deque

def solution(board, moves):
    m, n = len(board[0]), len(board)
    
    queue = [deque() for _ in range(m)]
    basket = []
    answer = 0
    
    for x in range(m):
        for y in range(n-1, -1, -1):
            if board[y][x] > 0:
                queue[x].append(board[y][x])
    
    for move in moves:
        move -= 1
        if queue[move]:
            doll = queue[move].pop()

            if basket and basket[-1] == doll:
                answer += 2
                basket.pop()
            else:
                basket.append(doll)
    
    return answer

# ----------

def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        move -= 1
        
        for line in board:
            if line[move] > 0:
                if basket and basket[-1] == line[move]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(line[move])
                
                line[move] = 0
                break            
            
    return answer