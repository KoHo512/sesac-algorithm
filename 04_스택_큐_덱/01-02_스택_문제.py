### 스택 관련 문제

## 데일리알고 81번: 스택
def solution(queries):
    answer = []
    stack = []

    for query in queries:
        if query == "pop":
            if stack:
                answer.append(stack.pop())
            else:
                answer.append(0)
        else:
            stack.append(int(query.split()[1]))
    
    return answer


## 백준 10773번: 제로
import sys

input = sys.stdin.readline

k = int(input())
numbers = []

for _ in range(k):
    num = int(input())

    if num == 0:
        numbers.pop()
    else:
        numbers.append(num)

print(sum(numbers))


## 백준 9012번: 괄호
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    check = []
    parenthesis = input()

    for ps in parenthesis:
        if ps == "(":
            check.append(ps)
        elif ps == ")":
            if not check:
                print("NO")
                break
            
            check.pop()
    else:
        if check:
            print("NO")
        else:
            print("YES")