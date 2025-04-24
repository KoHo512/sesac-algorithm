### 스택
## 파이썬에서는 리스트를 스택으로 사용

stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)    # [1, 2, 3]

# pop
print(stack.pop())  # 3
print(stack.pop())  # 2

# peek
print(stack[-1])    # 1


## 문제 풀기 (⇒ 01-02_스택_문제.py)
# 데일리알고 81번: 스택
# 백준 10773번: 제로
# 백준 9012번: 괄호