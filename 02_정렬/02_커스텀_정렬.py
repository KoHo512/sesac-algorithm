### 커스텀 정렬
# 내가 원하는 기준으로 정렬

## 1. 기본적인 방법을 이용한 커스텀 정렬
words = ["hello", "abc", "z"]

print(sorted(words))    # ['abc', 'hello', 'z']
# ⇒ 첫글자부터 abc 순으로 정렬됨

# 길이순으로 정렬하고 싶다면?
def length(word):
    return len(word)

sorted_words = sorted(words, key=length)
print(sorted_words)     # ['z', 'abc', 'hello']

# words.sort(key=length)


## 2. 리스트를 원소로 갖는 리스트 커스텀 정렬
numbers = [[1, 13], [2, 7], [1, 7], [5, 10], [4, 20]]

print(sorted(numbers))  # [[1, 7], [1, 13], [2, 7], [4, 20], [5, 10]]
# ⇒ 각 리스트의 첫번째 원소부터 오름차순으로 정렬됨

# 두 번째 원소 기준으로 정렬하고 싶다면? ⇒ [[2, 7], [1, 7], [5, 10], [1, 13], [4, 20]]
def second(number):
    return number[1]

sorted_numbers = sorted(numbers, key=second)
print(sorted_numbers)   # [[2, 7], [1, 7], [5, 10], [1, 13], [4, 20]]


# 두 번째 원소 기준으로,
# 만약 두 번째 원소가 같다면 첫 번째 원소를 기준으로 정렬하고 싶다면?
def sort_key(unit):
    return unit[1], unit[0]

sorted_numbers = sorted(numbers, key=sort_key)
print(sorted_numbers)   # [[1, 7], [2, 7], [5, 10], [1, 13], [4, 20]]


## 3. Lambda 활용하기
def sort_key(unit):
    return unit[1]

sort_key = lambda unit: unit[1]
# ⇒ 2개가 정확히 똑같음
# "lambda 매개변수: 리턴값"

print(sort_key([1,2]))  # 2


## 단어의 길이로 정렬
words = ["hello", "abc", "z"]

def length(word):
    return len(word)
sorted_words = sorted(words, key=length)
print(sorted_words) #['z', 'abc', 'hello']

sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words) #['z', 'abc', 'hello']

sorted_words = sorted(words, key=len)
print(sorted_words) #['z', 'abc', 'hello']


## 절대값 정렬
def solution(numbers):
    # 1. 기본적인 방법
    def absolute(number):
        if number < 0:
            number = -number
        return number

    result = sorted(numbers, key=absolute)

    # 2. lambda 이용: 삼항연산자
    result = sorted(numbers, key=lambda number: -number if number < 0 else number)

    # 3. 내장함수 abs 이용
    result = sorted(numbers, key=abs)

    return result