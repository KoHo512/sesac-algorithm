"""
두 자연수 numberA와 numberB를 더해 만들 수 있는 자연수 중 limit 이하인 자연수의 개수를 구하려 합니다. 
이때, numberA와 numberB를 동시에 사용하지 않고 둘 중 하나만 사용할 수 있습니다. 
예를 들어 2와 4로 10 이하의 수로 만들 수 있는 방법은 다음과 같다. 
 
2 = 2           방법 1 
4 = 4           방법 2 
2 + 2 = 4       중복 제외 
2 + 4 = 6       방법 3 
4 + 4 = 8       방법 4 
2 + 2 + 2 = 6   중복 제외 
2 + 2 + 4 = 8   중복 제외 
2 + 4 + 4 = 10  방법 5 
 
따라서 총 5개입니다. 
 
두 자연수 numberA와 numberB, limit가 solution 함수의 매개변수로 주어집니다. 
numberA와 numberB를 더해 만들 수 있는 자연수 중 limit 이하인 수의 개수를 return 하도록 
solution 함수를 완성해주세요. 
 
매개변수 설명 
두 자연수 numberA와 numberB, limit가 solution 함수의 매개변수로 주어집니다.  
- numberA와 numberB는 1 이상 100 이하인 자연수입니다. 
- limit는 1 이상 1,000 이하인 자연수입니다. 
 
return설명 
numberA와 numberB를 더해 만들 수 있는 자연수 중 limit 이하인 자연수의 개수를 return 해주세요.
"""

# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(numberA, numberB, limit):
    # 여기에 코드를 작성해주세요.
    # answer = [0] * 1001
    # return sum(answer[1:])

    answer = [0] * 1001

    def add_number(num1, num2):
        num1 += num2

        if num1 > limit:
            return
        
        if answer[num1] == 1:
            return
        
        answer[num1] = 1

        add_number(num1, numberA)
        add_number(num1, numberB)

    add_number(0, numberA)
    add_number(0, numberB)

    return sum(answer[1:])

# def solution(numberA, numberB, limit):
#     answer = [0] * 1001
#     answer[0] = 1

#     for number in range(min(numberA, numberB), limit + 1):
#         if number - numberA >= 0 and answer[number - numberA] == 1:
#             answer[number] = 1
        
#         if number - numberB >= 0 and answer[number - numberB] == 1:
#             answer[number] = 1
        
#     return sum(answer[1:])

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 
numberA1 = 2
numberB1 = 4
limit1 = 10
ret1 = solution(numberA1, numberB1, limit1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

numberA2 = 2
numberB2 = 3
limit2 = 10
ret2 = solution(numberA2, numberB2, limit2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")