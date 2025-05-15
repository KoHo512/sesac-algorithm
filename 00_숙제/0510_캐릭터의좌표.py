# 프로그래머스 120861번: 캐릭터의 좌표

def solution(keyinput, board):
    m, n = board
    
    x, y = 0, 0
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    
    for key in keyinput:
        # if key == "up":
        #     i = 0
        # elif key == "down":
        #     i = 1
        # elif key == "left":
        #     i = 2
        # else:
        #     i = 3
        i = { "up": 0, "down": 1, "left": 2, "right": 3 }.get(key)
        
        nx, ny = x + dx[i], y + dy[i]
        
        if - m / 2 <= nx <= m / 2 and - n / 2 <= ny <= n / 2:
            x, y = nx, ny
        
    return [x, y]