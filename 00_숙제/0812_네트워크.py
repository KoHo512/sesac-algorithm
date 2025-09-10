# 프로그래머스 43162번: 네트워크

def solution(n, computers):
    network = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
            
        for n_node in range(n):
            if node != n_node and computers[node][n_node] == 1 and not visited[n_node]:
                dfs(n_node)
                    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network += 1
                    
    return network