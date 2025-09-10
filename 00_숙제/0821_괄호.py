# 백준 9012번: 괄호

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ps = input()
    queue = deque()

    for p in ps:
        if p == "(":
            queue.append(p)
        elif p == ")":
            if not queue:
                print("NO")
                break

            queue.pop()
    else:
        if queue:
            print("NO")
        else:
            print("YES")
