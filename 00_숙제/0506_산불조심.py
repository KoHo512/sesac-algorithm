# 데일리알고 65번: 산불 조심

from collections import deque

def solution(mountain):  
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    n = len(mountain)
    visited = [[-1] * n for _ in range(n)]
    queue = deque()

    for x in range(n):
        for y in range(n):
            if mountain[x][y] == 2:
                visited[x][y] = 0
                queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and mountain[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return max(map(max, *visited))


# ----------
# 강사님 풀이

from collections import deque

def solution(mountain):

    def bfs():
        # queue = deque()

        # for i in range(n):
        #     for j in range(n):
        #         if mountain[i][j] == 2:
        #             queue.append((i, j, 0))

        queue = deque([(i, j, 0) for i in range(n) for j in range(n) if mountain[i][j] == 2])
        
        while queue:
            x, y, t = queue.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < n and 0 <= ny < n and mountain[nx][ny] == 0:
                    mountain[nx][ny] = 2  # 불이 옮겨붙음 == 방문처리
                    queue.append((nx, ny, t + 1))
        
        return t

    n = len(mountain)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
    
    answer = bfs()

    return answer