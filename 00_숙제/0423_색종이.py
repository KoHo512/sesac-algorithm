# 백준 2563번: 색종이

# import sys

# input = sys.stdin.readline

# n = int(input())
# papers = [list(map(int, input().split())) for _ in range(n)]
# area = 100 * n

# papers.sort()

# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if papers[i][0] + 10 <= papers[j][0]:
#             break

#         if -10 < papers[i][1] - papers[j][1] < 10:
#             x = papers[i][0] + 10 - papers[j][0]
#             y = min(papers[i][1] - papers[j][1], papers[j][1] - papers[i][0]) + 10
#             area -= x * y
#             # 3장 이상 겹치는 경우 겹치는 영역이 중복해서 빠진다..

# print(area)

# ----------
# 답지를 보고 아이디어 참고

# import sys

# input = sys.stdin.readline

# n = int(input())

# papers = [list(map(int, input().split())) for _ in range(n)]

# white_paper = [[0] * 100 for _ in range(100)]

# for paper in papers:
#     for i in range(paper[0], paper[0] + 10):
#         for j in range(paper[1], paper[1] + 10):
#             white_paper[i][j] = 1


# print(sum([sum(line) for line in white_paper]))

# ----------
# 답지를 보고 보완

import sys

input = sys.stdin.readline

n = int(input())

paper = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

print(sum(map(sum, paper)))