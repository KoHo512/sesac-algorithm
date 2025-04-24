### 덱

from collections import deque

queue = deque()

# enqueue (앞, 뒤)
queue.appendleft(1)
queue.appendleft(2)
queue.append(3)
queue.append(4)
print(queue)    # deque([2, 1, 3, 4])

# dequeue (앞, 뒤)
print(queue.popleft())  # 2
print(queue.pop())      # 4

# peek (앞, 뒤)
print(queue[0])     # 1
print(queue[-1])    # 3


# 하지만 deque가 무조건 빠른 건 아니고
# deque의 가운데에 있는 값을 조회할 때 불리


## 문제 풀기
# 데일리알고 83번: 큐
from collections import deque

def solution(queries):
    queue = deque()
    answer = []

    for query in queries:
        if query == "removeFirst":
            if queue:
                answer.append(queue.popleft())
            else:
                answer.append(0)
            continue

        if query == "removeLast":
            if queue:
                answer.append(queue.pop())
            else:
                answer.append(0)
            continue
        
        q, x = query.split()

        if q == "addFirst":
            queue.appendleft(int(x))
        else:
            queue.append(int(x))

    return answer