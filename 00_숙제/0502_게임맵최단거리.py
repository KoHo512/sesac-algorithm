# 프로그래머스 1844번: 게임 맵 최단거리

from collections import deque

def solution(maps):
    
    def bfs(x, y):
        queue = deque([(x, y, 1)])
        
        while queue:
            x, y, distance = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if nx == n - 1 and ny == m - 1:
                    nonlocal answer
                    answer = min(answer, distance + 1)
                    return
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))
                    
    n, m = len(maps), len(maps[0])
    x, y = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    answer = n * m
    
    visited[x][y] = True
    bfs(x, y)
    
    if answer == n * m:
        return -1
    
    return answer

# ⇒ 제출 시, 특정 테스트 케이스에서 실패
# 출발지에서 도착지까지 "거치는 칸"의 수를 구하는 문제이기 때문에
# 거치는 칸의 수가 n * m개인 맵이 존재할 수 있음
# answer를 n * m보다 큰 수(예: float("inf"))로 할당하면 통과함

# ----------
# 답안지 보고 보완

from collections import deque

def solution(maps):
    
    def bfs(x, y):
        queue = deque([(x, y)])
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    
                    if nx == n - 1 and ny == m - 1:
                        return visited[nx][ny]
                
                    queue.append((nx, ny))
        return -1
                    
    n, m = len(maps), len(maps[0])
    x, y = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0] * m for _ in range(n)]
    
    visited[x][y] = 1
    return bfs(x, y)

# ----------
# 처음에 풀었던 방식 보완

from collections import deque

def solution(maps):
    
    def bfs(x, y):
        queue = deque([(x, y, 1)])
        
        while queue:
            x, y, distance = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if nx == n - 1 and ny == m - 1:
                    return distance + 1
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))
                    
        return -1
                    
    n, m = len(maps), len(maps[0])
    x, y = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    
    visited[x][y] = True
    return bfs(x, y)