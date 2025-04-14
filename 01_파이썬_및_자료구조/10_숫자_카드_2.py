# 백준 10816번: 숫자 카드 2

import sys

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards_dict = {}

for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

M = int(input())
cards = list(map(int, input().split()))

# print(" ".join([str(cards_dict.get(card, 0)) for card in cards]))

answer = [cards_dict.get(card, 0) for card in cards]
print(*answer, sep=" ")

# ----------
# 강사님 풀이

import sys

from collections import Counter

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

# counter = {}

# for card in cards:
#     if card in counter:
#         counter[card] += 1
#     else:
#         counter[card] = 1
counter = Counter(cards)

for number in numbers:
    counts = counter.get(number, 0)
    print(counts, end=" ")