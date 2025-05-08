### 조합 관련 문제
## 백준 6603번: 로또

import sys

input = sys.stdin.readline

while True:
    k, *s = map(int, input().rsplit())

    if k == 0:
        break

    def combinations(current, start):
        if len(current) == 6:
            print(*current)
            return
        
        for i in range(start, k):
            current.append(s[i])
            combinations(current, i + 1)
            current.pop()

    combinations([], 0)

    print()