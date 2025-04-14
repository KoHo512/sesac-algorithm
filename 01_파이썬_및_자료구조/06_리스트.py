### 리스트

## 1. append
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]
# ⇒ 시간복잡도: O(1)


## 2. pop
numbers = [1, 2, 3]
number = numbers.pop()
print(numbers)  # [1, 2]
print(number)   # 3
# ⇒ 시간복잡도: O(1)

numbers = [1, 2, 3]
number = numbers.pop(0)
print(numbers)  # [2, 3]
print(number)   # 1
# ⇒ 시간복잡도: O(n)


## 3. count
numbers = [1, 2, 2, 3]
counts = numbers.count(2)
print(counts)   # 2
# ⇒ 시간복잡도: O(n)


## 4. sort
numbers = [4, -1, 0, 2, 100]
numbers.sort()
print(numbers)  # [-1, 0, 2, 4, 100]
# ⇒ 시간복잡도: O(nlogn)

numbers.sort(reverse=True)
print(numbers)  # [100, 4, 2, 0, -1]
# ⇒ 시간복잡도: O(nlogn)