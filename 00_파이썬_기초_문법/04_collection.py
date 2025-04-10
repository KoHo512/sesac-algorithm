### 컬렉션(Collection)

# List<Integer> list = new ArrayList<>();

# 주의: 예약어(키워드)는 변수명으로 사용 불가
# ex) int, float, str, boolean, true, false, if, for, ...
#   sum, max, min, len, ...
# => 대체: list_, sum_, ...

list_ = []      # 빈 리스트
list_ = list()  # 빈 리스트


## Function vs. Method
# 메서드(필드 함수)는 특정 객체(자료형)에 종속
# 함수는 특정 객체에 종속 X, 오류는 발생

# 리스트의 기능(메서드)
# 값 추가, 삭제, 정렬 등


## 리스트에 값 추가하기
list_ = []

# 리스트 마지막에 값을 하나만 추가 (한번에 여러개 추가 불가)
list_.append(1)   
print(list_)    # [1]

# 리스트의 특정 위치에 값을 하나만 추가
list_.insert(0, 0)
print(list_)    # [0, 1]

list_.insert(1, 2)
print(list_)    # [0, 2, 1] 
# => insert()는 느려서 잘 사용하지 않음

## 리스트의 값 삭제하기
# 리스트 마지막의 값 삭제하고 반환
list_.pop()
print(list_)    # [0, 2]

pop_item = list_.pop()
print(pop_item) # 2

# 리스트 특정 위치의 값 꺼내기
list_.append(1)
list_.append(2)
list_.append(3)
list_.append(4)
print(list_)    # [0, 1, 2, 3, 4]

# 두번째 위치(인덱스=1)의 값(숫자 1)을 꺼내오고 싶다
pop_item = list_.pop(1)
print(pop_item) # 1
# => 특정 위치에 값을 넣거나,  특정 위치의 값을 빼오는 건 느림


## 리스트의 슬라이싱
# 리스트의 일부분을 자르는 연산
# 리스트[시작:끝:간격]

# 시작부터 세번째까지 1의 간격으로 슬라이싱
# for (int i = 0; i < end; i++) 
print(list_)            # [0, 2, 3, 4]
print(list_[0:3:1])     # [0, 2, 3]

# for (int i = 2; i > 3; i__)
print(list_[3:1:-1])    # [4, 3]

# 시작, 간격은 생략 가능
# 생략하면 시작은 0, 간격은 1이 기본값
print(list_[:3])        # [0, 2, 3]

# 끝, 간격은 생략 가능
# 생략하면 끝은 마지막까지, 간격은 1이 기본값
print(list_[1:])        # [2, 3, 4]


## 리스트의 레인지(range)
# 특정 범위의 정수 리스트 생성
# for (초기값: 조건식: 종감문)
# for (int i = 0; i < 10; i++)
range(0, 10, 1)     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(0, 10, 1))          # range(0, 10)
print(list(range(0, 10, 1)))    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for (int i = 1, i < 11; i = i + 2)
range(1, 11, 2)     # [1, 3, 5, 7, 9]

# 주의: 실수는 넣을 수 없음


## 튜플(Tuple)
# 수정이 불가능한(immutable) 리스트


## 리스트 <-> 문자열 형 변환
list1 = ["1", "2", "3", "4"]
str1 = "1234"

list2 = list(str1)  # 문자열 -> 리스트 변환
str2 = str(list1)   # 리스트 -> 문자열 변환

print(list2)    # ['1', '2', '3', '4']
print(str2)     # ['1', '2', '3', '4'] (리스트 -> 문자열)

# str2에 대해 예상했던 결과는 "1234"인데?
# 해결하는 방법
# 1) 반복문
# 2) join()
# str.join("구분자", 리스트)
str3 = str.join("", list1)
print(str3)     # 1234

str4 = str.join("+", list1)
print(str4)     # 1+2+3+4


## 딕셔너리 -> JS 객체(object)


## 집합(Set)
# 집합은 수학에서의 집합의 특징을 가진 자료형
# 리스트와 다른 점
# 1. 중복된 값을 저장할 수 없음
# 2. 순서가 없음

# 빈 set 생성
# s = {}는 빈 딕셔너리를 의미하기 때문에 set()으로 생성해야함
set_ = set()

# 값이 있는 set 생성
set_ = {1, 2, 2, 3}
print(set_)     # {1, 2, 3} => 중복된 값은 들어가지 않음

# 문제. 리스트에서 중복을 제외한 수의 개수를 반환하시오.
list_ = [1, 2, 3, 4, 3, 12, 3, 5, 5, 3, 2, 5, 6, 1]
print(set(list_))       # {1, 2, 3, 4, 5, 6, 12}
print(len(set(list_)))  # 7

# 집합 자료형은 인덱싱 X
print({1, 2, 3})