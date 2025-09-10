#백준 2164번: 카드2

import sys

input = sys.stdin.readline

n = int(input())
cards = [i for i in range(1, n + 1)]

for _ in range(n - 1):
    cards = cards[2:] + [cards[1]]

print(cards[0])

# ⇒ 시간 초과 발생

# ----------

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = deque(range(1, n + 1))

for _ in range(n - 1):
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])