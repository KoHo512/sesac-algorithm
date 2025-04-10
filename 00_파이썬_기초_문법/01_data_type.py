### 기본 자료형

## 변수 생성
# 자바의 변수 생성
# 자료형 변수 이름
# int number;

# 파이썬의 변수 생성
# 파이썬은 자료형을 따로 명시하지 않음
# 변수 이름 = 할당할 값
a = 0       # 정수형(int) 변수
b = 1.1     # 실수형(float) 변수


## 자바와 파이썬의 문자열 비교
# 자바
# 'a' => 문자(char)
# "abcd" => 문자열(String)

# 파이썬
# 'a' => 문자열(String)
# "a" => 문자열(String)
# 주의: 혼용은 안 됨! ('" -> X / "' -> X)

# "": 빈 문자열 => 문자열
# " ": 공백만 있는 문자열 => 문자열


# 자바스크립트 문자열 리터럴 `${variable}`
# 파이썬 문자열 포멧팅 f-string
print(f"1 + 1 = {1 + 1}")   # 1 + 1 = 2

name = "KoHo"
print(f"이름은 {name}입니다.")  # 이름은 KoHo입니다.


## boolean형
# True / False
# 어떤 경우에 False인가?
# - 정수형(int)은 0일 때
# - 실수형(float)은 0.0일 때
# - 문자열(String)은 빈 문자열("")일 때
# - 리스트(list)는 빈 리스트([])일 때
# - 딕셔너리(dictionary)는 빈 딕셔너리({})일 때
# => 비어있으면 False


## 기본 자료형 간의 형 변환
number1 = 1
number2 = float(number1)
print(number1, number2)     # 1 1.0

number3 = 1.1
number4 = int(number3)      # 내림을 해서 정수 부분만 사용
print(number3, number4)     # 1.1 1

# [번외] 반올림을 하고 싶다면?
number5 = 1.1
number6 = int(number5 + 0.5)
print(number3, number4)     # 1.1 1

# 문자열 -> 숫자형 변환
# 주의: 숫자형 형태의 문자열이 아니면 변환 불가능
str1 = "a"
# int(str1)     # ValueError: invalid literal for int() with base 10: 'a'

str2 = "1"
print(int(str2))    # 1

str3 = "1.1"
print(float(str3))      # 1.1
# int(str3)     # ValueError: invalid literal for int() with base 10: '1.1'
print(int(float(str3))) # 1