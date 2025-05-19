# 백준 1753번: 최단경로

import sys

input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0

    for _ in range(v - 1):
        node, min_dist = -1, INF

        for i in range(v + 1):
            if not visited[i] and distance[i] < min_dist:
                node = i
                min_dist = distance[i]

            visited[node] = True

            for next_node, dist in graph[node]:
                next_dist = distance[node] + dist

                if not visited[next_node] and next_dist < distance[next_node]:
                    distance[next_node] = next_dist


v, e = map(int, input().split())
start = int(input())

INF = float("inf")
distance = [INF] * (v + 1)
visited = [False] * (v + 1)

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start)

for dist in distance[1:]:
    if dist == INF:
        print("INF")
    else:
        print(dist)


# ⇒ 시간 초과 발생