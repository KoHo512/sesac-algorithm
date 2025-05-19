# 백준 1916번: 최소비용 구하기

import sys

input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0

    for _ in range(n - 1):
        node, min_dist = -1, INF

        for i in range(n + 1):
            if not visited[i] and distance[i] < min_dist:
                node = i
                min_dist = distance[i]
        
        visited[node] = True

        # 백트래킹
        if node == end:
            return

        for next_node, dist in graph[node]:
            next_dist = distance[node] + dist

            if not visited[next_node] and next_dist < distance[next_node]:
                distance[next_node] = next_dist


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

INF = float("inf")
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])