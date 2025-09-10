"""
네 자리 자연수를 조합하여 만든 가장 큰 수와 가장 작은 수의 차이 값을 구하려 합니다.  
예를 들어, 5924의 자연수가 주어질 때 가장 큰 수의 조합은 9542이고 가장 작은 수의 조합은 2459입니다. 
두 숫자의 차이 값은 7083을 출력합니다. 
네 자리 자연수를 담은 num이 solution 함수의 매개변수로 주어질 때, 
가장 큰 차이 값을 return하도록 solution 함수를 작성하려 합니다.  
빈칸을 채워 전체 코드를 완성해주세요. 

매개변수 설명 
네 자리 자연수를 담은 num이 solution 함수의 매개변수로 주어집니다. - num은 1000 이상 9999 이하인 자연수입니다. 

return 설명 
네 자리 자연수를 조합하여 만든 가장 큰 수와 가장 작은 수의 차이 값을 return 합니다.
"""

# import math

def maxNumber(value):
    # digits = [[quiz]]
    # digits.sort([[quiz]])
    # return [[quiz]]
    digits = [v for v in str(value)]    # list(str(value))
    digits.sort(reverse=True)
    return int("".join(digits))

def minNumber(value):
    # digits = [[quiz]]
    # digits.sort([[quiz]])
    # return [[quiz]]
    digits = [v for v in str(value)]
    digits.sort()
    return int("".join(digits))

def solution(num):
    answer = 0
    maxNum = maxNumber(num)
    minNum = minNumber(num)

    # answer = [[quiz]]
    answer = maxNum - minNum
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num1 = 5924
ret1 = solution(num1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num2 = 3904
ret2 = solution(num2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")