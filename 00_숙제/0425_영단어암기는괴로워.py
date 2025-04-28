# 백준 20920번: 영단어 암기는 괴로워

import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())

words = []

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        words.append(word)

counter = Counter(words)

def sort_word(word):
    return -counter[word], -len(word), word

words = sorted(set(words), key=sort_word)

for word in words:
    print(word)


# ----------
# 답안지를 보고 보완

import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]

counter = Counter(words)
results = sorted(set(words), key=lambda word: (-counter[word], -len(word), word))

for word in results:
    if len(word) >= m:
        print(word)