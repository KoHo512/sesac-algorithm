### 델타 탐색 관련 문제

## 데일리알고 71번: 이차원 배열의 델타 탐색 1
def solution(numbers, r, c):
    n = len(numbers)
    m = len(numbers[0])
    total = 0

    # 1. 기준점 잡기
    x = r - 1
    y = c - 1

    # 2. 델타값 정의 (상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 3. 이동하기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 4. 범위 확인
        if 0 <= nx < n and 0<= ny < m:
            total += numbers[nx][ny]

    return total


## 데일리알고 72번: 이차원 배열의 델타 탐색 2
def solution(numbers):
    answer = 0
    n = len(numbers)
    m = len(numbers[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x in range(n):
        for y in range(m):
            # flag = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            #     if 0 <= nx < n and 0 <= ny < m:
            #         if numbers[x][y] < numbers[nx][ny]:
            #             flag = False
            #             break

            # if flag: 
            #     answer += 1

                if 0 <= nx < n and 0 <= ny < m and numbers[x][y] < numbers[nx][ny]:
                    break
            else:
                answer += 1

    return answer


## 데일리알고 73번: 로봇 여행 게임 1
def solution(board, queries):
    n = len(board)
    m = len(board[0])
    total = 0
    
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, -1, 1]

    x, y = 0, 0

    for query in queries:
        if query == "Get Score":
            total += board[x][y]
            continue
            # 로봇의 위치는 변하지 않으니까, 아래의 이동 로직은 실행하지 않음

        if query == "Move Up":
            direction = 0
        elif query == "Move Down":
            direction = 1
        elif query == "Move Left":
            direction = 2
        elif query == "Move Right":
            direction = 3

        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <= ny < m:
            x = nx
            y = ny

    return total


## 데일리알고 74번: 로봇 여행 게임 2
def solution(board, queries):
    n = len(board)
    m = len(board[0])
    total = 0

    x, y = 0, 0

    # 델타값 정의 (하우상좌)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    direction = 0

    for query in queries:
        if query == "Get Score":
            total += board[x][y]
            continue

        if query == "Turn Left":
            direction = (direction + 1) % 4
            continue
        elif query == "Turn Right":
            direction = (direction - 1) % 4
            continue

        # if query == "Move Backward":
        #     move_direction = (direction + 2) % 4
        # else:
        #     move_direction = direction

        # nx = x + dx[move_direction]
        # ny = y + dy[move_direction]

        if query == "Move Forward":
            nx = x + dx[direction]
            ny = y + dy[direction]
        elif query == "Move Backward":
            nx = x - dx[direction]
            ny = y - dy[direction]

        if 0 <= nx < n and 0 <= ny < m:
            x = nx
            y = ny

    return total