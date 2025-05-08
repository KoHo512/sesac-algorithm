# 데일리알고 62번: 미로 찾기 1

from collections import deque

def solution(maze):
    def bfs(x, y):
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx == n - 1 and ny == n - 1:
                    nonlocal answer
                    answer = True
                    return

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    n = len(maze)
    x, y = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    visited = [[False] * n for _ in range(n)]
    answer = False

    visited[x][y] = True
    bfs(x, y)

    return answer