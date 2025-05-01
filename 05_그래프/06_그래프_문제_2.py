### 그래프 관련 문제

## 백준 2667번: 단지번호붙이기
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
matrix = [[int(digit) for digit in input().rstrip()] for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

complex = 0
apts = []

def bfs(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1:
                    global apt_num
                    apt_num += 1
                    matrix[nx][ny] = 2
                    queue.append((nx, ny))

for x in range(n):
    for y in range(n):
        if matrix[x][y] == 1:
            complex += 1
            apt_num = 0
            bfs(x, y)
            apts.append(apt_num)

print(complex)
for number in sorted(apts):
    print(number)

# 예제는 잘 되는데 제출하면 틀렸다고 뜸..
# ⇒ bfs/dfs 시작 전에 matrix[x][y]를 세팅하지 않아서 문제가 발생한 거였음
# bfs/dfs 탐색을 하다보면 결국 방문은 돼서 예제는 성공한 거 같고
# 아마 단지에 속하는 집의 수가 1인 단지가 있는 테스트 케이스에서 틀린듯

# ----------
# 강사님 풀이
import sys

input = sys.stdin.readline

def dfs(x, y):
    global house
    house += 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            board[nx][ny] = 0
            dfs(nx, ny)

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []

for x in range(n):
    for y in range(n):
        if board[x][y] == 1:
            house = 0
            board[x][y] = 0
            dfs(x, y)
            result.append(house)

print(len(result))
print(*sorted(result), sep="\n")

# ----------
# 보완
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
matrix = [[int(digit) for digit in input().rstrip()] for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

apts = []

def bfs(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1:
                    global apt_num
                    apt_num += 1
                    matrix[nx][ny] = 2
                    queue.append((nx, ny))

for x in range(n):
    for y in range(n):
        if matrix[x][y] == 1:
            apt_num = 1
            matrix[x][y] = 2
            bfs(x, y)
            apts.append(apt_num)

print(len(apts))
for number in sorted(apts):
    print(number)


# 다음 주까지 데일리알고 65번: 산불조심 풀어보기 