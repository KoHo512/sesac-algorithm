## 백준 10971번: 외판원 순회 2
# 한붓 그리기

import sys

input = sys.stdin.readline

# city: 현재 몇 번째 도시인지(도시 번호)
# depth: 현재 몇 개의 도시를 탐색했는지
# cost: 현재 도시까지 왔을 때의 총 비용
def permutations(city, depth, cost):
    # 1. 종료 조건
    if depth == n - 1 and w[city][0] > 0:
        global min_cost
        min_cost = min(min_cost, cost + w[city][0])
        return
    
    # 2. 점화식
    for next_city in range(n):
        if not visited[next_city] and w[city][next_city] > 0:
            visited[next_city] = True
            permutations(next_city, depth + 1, cost + w[city][next_city])
            visited[next_city] = False

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_cost = 10_000_000  # 최악의 상황의 비용: 최대 도시 수(10) * 도시 이동 최대 비용(1_000_000)

visited[0] = True
permutations(0, 0, 0)

print(min_cost)

# ⇒ 통과는 하지만,
# cost가 이미 min_cost보다 큰 경우에도 탐색 진행 (비효율적)

# ----------
# 백트래킹 추가

import sys

input = sys.stdin.readline

# city: 현재 몇 번째 도시인지(도시 번호)
# depth: 현재 몇 개의 도시를 탐색했는지
# cost: 현재 도시까지 왔을 때의 총 비용
def permutations(city, depth, cost):
    global min_cost

    # 백트래킹
    if cost >= min_cost:
        return
    
    # 1. 종료 조건
    if depth == n - 1 and w[city][0] > 0:
        min_cost = min(min_cost, cost + w[city][0])
        return
    
    # 2. 점화식
    for next_city in range(n):
        if not visited[next_city] and w[city][next_city] > 0:
            visited[next_city] = True
            permutations(next_city, depth + 1, cost + w[city][next_city])
            visited[next_city] = False

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_cost = 10_000_000  # 최악의 상황의 비용: 최대 도시 수(10) * 도시 이동 최대 비용(1_000_000)

visited[0] = True
permutations(0, 0, 0)

print(min_cost)


## 숙제: 데일리알고 97번: N Rook Problem 풀어보기
# 순열과 조합 문제인데 왜 순열과 조합인지 고민