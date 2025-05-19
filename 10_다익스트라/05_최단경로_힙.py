# 백준 1753번: 최단경로

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distance[node]:
            continue

        for next_node, dist in graph[node]:
            next_dist = min_dist + dist

            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))


v, e = map(int, input().split())
start = int(input())

INF = float("inf")
distance = [INF] * (v + 1)

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