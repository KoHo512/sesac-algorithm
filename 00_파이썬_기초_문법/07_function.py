### 함수(Function)
# 자바스크립트
"""
const func = () => {
    코드
}
function func() {
    코드
}
"""

# 자바
"""
function func() {
    코드
}
"""

# 파이썬 함수 정의
# def 키워드 활용
# 중괄호 x => 들여쓰기로 코드 블럭 구분
# 콜론(:)으로 함수 정의부 나타냄
def func(parameter):
    print(f"함수 실행, {parameter}")
    return parameter + 1

# 함수 호출
return_value = func(10)     # 함수 실행, 10
print(return_value)         # 11
