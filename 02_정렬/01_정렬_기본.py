### 정렬

## 오름차순 정렬
# 내장함수 sorted() 이용 / 리스트 메서드 .sort() 이용
numbers = [1, 3, -4, 0, 100]
sorted_numbers = sorted(numbers)
print(numbers)          # [1, 3, -4, 0, 100]
print(sorted_numbers)   # [-4, 0, 1, 3, 100]
# ⇒ 원본은 변경되지 않고 정렬된 리스트 반환
# 리스트가 아닌 정렬 가능한 다른 자료형(set, tuple, ...)도 가능

numbers = [1, 3, -4, 0, 100]
numbers.sort()
print(numbers)  # [-4, 0, 1, 3, 100]
# ⇒ 원본 리스트가 변경
# 리스트는 mutable 자료형이기 때문
# 리스트에만 적용됨


## 내림차순 정렬
# reverse 조건만 추가하면 됨
numbers = [1, 3, -4, 0, 100]
sorted_numbers = sorted(numbers, reverse=True)
print(numbers)          # [1, 3, -4, 0, 100]
print(sorted_numbers)   # [100, 3, 1, 0, -4]

numbers = [1, 3, -4, 0, 100]
numbers.sort(reverse=True)
print(numbers)  # [100, 3, 1, 0, -4]
