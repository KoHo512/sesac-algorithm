### 큐
## 파이썬에서는 큐도 리스트로 구현

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)    # [1, 2, 3]

# dequeue
print(queue.pop(0)) # 1
print(queue.pop(0)) # 2

# peek
print(queue[0])


## 문제 풀기
# # 데일리알고 82번: 큐
def solution(queries):
    queue = []
    answer = []

    for query in queries:
        if query == "pop":
            if queue:
                answer.append(queue.pop(0))
            else:
                answer.append(0)
        else:
            queue.append(int(query.split()[1]))

    return answer


# pop(0)은 시간 복잡도가 O(n)
# 리스트(스택, 큐)의 데이터가 많을수록 많은 시간 소요
# ⇒ 앞으로 deque를 사용