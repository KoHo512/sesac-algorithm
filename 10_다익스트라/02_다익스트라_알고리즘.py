# 데일리알고 29번: [대표 유형] 다익스트라 알고리즘

def solution(n, edges):
    
    def dijkstra(start):
        # 3. distance[출발점] = 0 할당
        distance[start] = 0

        # n - 1번만 탐색해도 n번째 정점에 대한 최단 거리 확정됨
        for _ in range(n - 1):
            # 4. distance에서 최솟값 찾음
            node, min_dist = -1, INF

            for i in range(1, n + 1):
                if not visited[i] and min_dist > distance[i]:
                    node = i
                    min_dist = distance[i]

            # 5. 최소 거리 노드에 대해 거리 확정
            visited[node] = True

            # 6. 인접 노드들에 대해 거리를 더 작은 값으로 갱신
            for next_node, dist in graph[node]:
                next_dist = distance[node] + dist

                if not visited[next_node] and next_dist < distance[next_node]:
                    distance[next_node] = next_dist


    # 1. distance를 모두 무한대로 초기화
    INF = float("inf")
    distance = [INF] * (n + 1)

    # 2. visited를 모두 False로 초기화
    visited = [False] * (n + 1)

    graph = [[] for _ in range(n + 1)]

    for x, y, w in edges:
        graph[x].append((y, w))

    dijkstra(1)
    
    return distance[n]