### 컨테이너 자료형
## 1. 순서가 있는 자료형 vs 순서가 없는 자료형
## 2. 변경 가능한 자료형 vs 변경이 불가능한 자료형

## 3. 할당 vs 얕은 복사 vs 깊은 복사
# 3-1. 할당
a = [1, 2, 3]
b = a       # 할당
print(a)    # [1, 2, 3]
print(b)    # [1, 2, 3]

b[0] = 4
print(a)    # [4, 2, 3]
print(b)    # [4, 2, 3]

# ----------

a = "hello"
b = a       # 할당
print(a)    # hello
print(b)    # hello

b += "!"
print(a)    # hello
print(b)    # hello!
# ⇒ mutable과 immutable의 차이


# 3-2. 얕은 복사
from copy import copy

a = [1, 2, 3]
b = a[:]        # 복제 1
b = list(a)     # 복제 2
b = copy(a)     # 복제 3

b[0] = 4
print(a)    # [1, 2, 3]
print(b)    # [4, 2, 3]


# 3-3. 깊은 복사(deep copy)
# 얕은 복사의 한계 때문에 필요
a = [[1, 2, 3], [4, 5, 6]]
b = a[:]

b[0][0] = 9
print(a)    # [[9, 2, 3], [4, 5, 6]]
print(b)    # [[9, 2, 3], [4, 5, 6]]

# ----------

from copy import deepcopy
a = [[1, 2, 3], [4, 5, 6]]
b = deepcopy(a)

b[0][0] = 9
print(a)    # [[1, 2, 3], [4, 5, 6]]
print(b)    # [[9, 2, 3], [4, 5, 6]]