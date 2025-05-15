# 데일리알고 86번: [대표 유형] 최소 신장 트리(Minimum Spanning Tree)

def solution(n, edges):

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        
        return parent[x]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)

        if x_root == y_root:    # 사이클이 있음
            return False

        if rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        elif rank[x_root] < y_root:
            parent[x_root] = y_root
        else:
            parent[x_root] = y_root
            rank[y_root] += 1
        
        return True

    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    total = 0   # 비용의 총합
    counts = 0  # 간선의 갯수

    # 1. 가중치에 따라 간선을 오름차순으로 정렬
    edges.sort(key=lambda x: x[2])

    # 2. 가장 적은 비용의 간선부터 차례로 선택
    for x, y, w in edges:
        if union(x, y): # 사이클이 없으면
            total += w
            counts += 1

            if counts == n - 1: # 백트래킹
                break
    
    return total
