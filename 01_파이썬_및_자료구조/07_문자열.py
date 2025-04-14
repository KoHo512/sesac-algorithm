### 문자열

## 1. join
numbers = ["h", "e", "l", "l", "o"]
joined_numbers = "".join(numbers)
print(joined_numbers)   # hello

numbers = ["h", "e", "l", "l", "o"]
joined_numbers = "$".join(numbers)
print(joined_numbers)   # h$e$l$l$o

numbers = ["h", "e", "l", "l", "o"]
print("\n".join(numbers))
"""
h
e
l
l
o
"""


## 2. replace
word = "hello python"
new_word = word.replace("python", "java")
print(word)         # hello python
print(new_word)     # hello java
# ⇒ String은 immutable이라 원본 변경 불가능하고 바뀐 문자열을 반환


## 3. 슬라이싱 string[start:end:step]
word = "hello"
print(word[1:3])    # el
print(word[0:4:2])  # hl
print(word[3:1:-1]) # ll
print(word[::-1])   # olleh