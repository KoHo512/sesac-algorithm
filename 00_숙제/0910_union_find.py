parent = [0, 1, 2, 3, 4, 5]

def find(x):
    if parent[x] == x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x_root, y_root = find(x), find(y)

    if x_root == y_root:
        return
    
    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root