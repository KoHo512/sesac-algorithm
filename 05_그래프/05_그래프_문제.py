### 그래프 관련 문제

## 프로그래머스 43165번: 타겟 넘버

def solution(numbers, target):
    
    def dfs(depth, total):
        # 1. 종료 조건
        if depth == len(numbers):
            if total == target:
                nonlocal answer
                answer += 1
            return
        
        # 2. 정화식(재귀식)
        dfs(depth + 1, total + numbers[depth])
        dfs(depth + 1, total - numbers[depth])
        
    answer = 0
    dfs(0, 0)
    
    return answer


## 데일리알고 62번: 미로 찾기 1
import sys
sys.setrecursionlimit(10**6)

def solution(maze):

    def dfs(x, y):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx == n - 1 and ny == n - 1:
                nonlocal answer
                answer = True
                return

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] == 0:
                visited[nx][ny] = True
                dfs(nx, ny)

    n = len(maze)
    x, y = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * n for _ in range(n)]
    answer = False

    visited[x][y] = True
    dfs(x, y)

    return answer


## 데일리알고 63번: 미로 찾기 2
# 첫번째 방법: DFS 이용
import sys
sys.setrecursionlimit(10**6)

def solution(maze):
    def dfs(x, y, depth):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx == n - 1 and ny == n - 1:
                nonlocal answer
                answer = min(answer, depth + 1)
                return

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] == 0:
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1)
                # 모든 경우의 수를 확인해야해서 방문 처리를 취소해야 함
                visited[nx][ny] = False

    n = len(maze)
    x, y = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * n for _ in range(n)]
    answer = n * n

    visited[x][y] = True
    dfs(x, y, 0)

    return answer
# ⇒ 시간 초과 발생: 모든 경우의 수에서 깊이를 끝까지 확인해 비효율적

# 두번째 방법: BFS 이용
from collections import deque

def solution(maze):
    def bfs(x, y):
        queue = deque([(x, y, 0)])

        while queue:
            x, y, distance = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx == n - 1 and ny == n - 1:
                    nonlocal answer
                    answer = min(answer, distance + 1)
                    return

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))


    n = len(maze)
    x, y = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * n for _ in range(n)]
    answer = n * n

    visited[x][y] = True
    bfs(x, y)

    return answer

## DFS와 BFS의 시간 복잡도
# O(V + E)
# V: 정점의 개수 / E: 간선의 개수
# 단, 각 정점을 한번씩만 방문한다는 가정 하에
# 첫번째 방법에서 방문 처리를 취소하기 때문에 시간 초과가 되는 것

# 미로 찾기 1도 BFS로 풀어보기