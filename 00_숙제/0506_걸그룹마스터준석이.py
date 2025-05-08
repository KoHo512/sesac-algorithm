# 백준 16165번: 걸그룹 마스터 준석이

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
groups = {}

for _ in range(n):
    name = input().rstrip()
    groups[name] = sorted([input().rstrip() for _ in range(int(input().rstrip()))])

for _ in range(m):
    name = input().rstrip()
    quiz = int(input().rstrip())

    if quiz:
        for group in groups:
            if name in groups[group]:
                print(group)
                break
    else:
        print(*groups[name], sep="\n")