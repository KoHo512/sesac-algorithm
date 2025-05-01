# 데일리알고 75번: 달팽이 순회

def solution(n):
    matrix = [[0] * n for _ in range(n)]

    # 델타탐색 (우하좌상)
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    d = 0
    
    x, y = 0, 0
    matrix[x][y] = 1

    for i in range(2, n * n + 1):
        nx, ny = x + dx[d], y + dy[d]

        if not (0 <= nx < n and 0 <= ny < n and not matrix[nx][ny]):
            d = (d + 1) % 4
            nx, ny = x + dx[d], y + dy[d]

        x, y = nx, ny
        matrix[x][y] = i

    return matrix