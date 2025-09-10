"""
주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요. 
그러나, 코드 일부분이 잘못되어 있기 때문에 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 
OO카페에서는 매달 마지막날 2개의 음료에 대해 반값 할인행사를 하는데, 
반값 할인행사의 대상이 되는 음료는 고객들의 투표로 결정됩니다. 
반값 할인행사를 하기 위한 음료를 결정하기 위한 투표는 
매달 15일 OO카페 어플에서 진행되며, 가입된 ID당 1번씩 투표할 수 있습니다. 
투표 대상이 되는 후보 음료들은 카페에서 선정합니다. 
이 투표에서 첫번째로 많이 득표한 음료와 두번째로 많이 득표한 음료가 반값 할인행사의 대상 음료가 됩니다. 
반값 할인행사 대상이 되는 2개의 음료가 무엇인지를 알고자 합니다. 
후보 음료의 이름이 나열된 배열 menu와 고객들이 투표한 용지에 작성한 음료 이름을 나열한 배열 votes가 
solution 함수의 매개변수로 주어집니다. 
투표에서 첫번째로 득표한 음료의 이름과 두번째로 득표한 음료의 이름을 순서대로 return하세요. 
 
매개변수 설명 
- menu의 길이는 2 이상 10 이하입니다. 
- votes의 길이는 3 이상 1000 이하입니다. 
- menu와 votes의 원소는 알파벳 대문자와 소문자로 이루어진 문자열이며, 길이는 1 이상 50 이하입니다. 
- 투표 결과로 첫번째 득표한 음료와 두번째 득표한 음료를 항상 구할 수 있습니다. 
 
return 값 설명 
투표 결과로 첫번째 득표한 음료와 두번째 득표한 음료를 return 합니다. 
"""

def func_a(arr):
    answer = -1
    for i in range(len(arr)):
        if answer == -1:
            answer = i
        elif arr[answer] < arr[i]:
            answer = i
    return answer


def func_b(arr1, arr2):
    answer = [0] * len(arr1)
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                answer[i] += 1
    return answer


def func_c(arr, count):
    answer = -1
    for idx, elem in enumerate(arr):
        if elem == count:
            continue
        if answer == -1:
            answer = idx
        elif arr[answer] < elem:
            # answer += 1
            answer = idx
    return answer


def solution(menu, votes):
    counter = func_b(menu, votes)
    first = func_a(counter)
    second = func_c(counter, counter[first])

    answer = [menu[first], menu[second]]
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
menu = ["Latte", "Americano","Espresso" ]
votes = ["Latte", "Americano", "Espresso", "Latte", "Americano", "Americano", "Latte", "Americano", "Americano", "Latte", "Latte", "Latte"]
ret = solution(menu, votes)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

menu = ["MochaLatte", "GreenTea", "Cappuccino"]
votes = ["GreenTea", "GreenTea", "MochaLatte", "GreenTea", "Cappuccino", "Cappuccino"]
ret = solution(menu, votes)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")