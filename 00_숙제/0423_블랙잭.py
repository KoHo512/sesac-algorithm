# 백준 2798번: 블랙잭

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

max = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        sum = cards[i] + cards[j]
        if sum >= m:
            continue

        for k in range(j + 1, n):
            sum = cards[i] + cards[j] + cards[k]
            if max < sum <= m:
                max = sum

print(max)