# 데일리알고 90번: [대표 유형] 유니온 파인드 알고리즘(Union-Find Algorithm)

def solution(n, queries):
    
    def find(x):
        while x != parent[x]:
            x = parent[x]
        
        return x

    def union(x, y):
        x_root = find(x)
        y_root = find(y)

        if x_root == y_root:
            return

        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root

    parent = list(range(n + 1))
    answer = []

    for command, x, y in queries:
        if command == -1:
            union(x, y)
        else:
            if find(x) == find(y):
                answer.append(True)
            else:
                answer.append(False)

    return answer