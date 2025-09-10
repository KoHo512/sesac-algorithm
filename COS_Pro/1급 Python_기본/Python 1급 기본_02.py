"""
홍길동씨는 차량을 구매하려고 하는데, 
최근 유류비가 너무 많이 올라 운행가능거리가 가장 긴 차량을 구입하려고 합니다. 
1달동안 동일한 차량 운행 비용으로 유류를 모두 구매하여, 
이를 모두 사용했을 시에 운행가능거리가 가장 긴 차량을 알고자 합니다. 
홍길동씨가 구매하려고 하는 차량의 이름 리스트 name, 
한달동안 차량 운행을 위해 사용할 수 있는 금액 money, 
구매하려고 하는 차량의 연비와 유류비 항목을 나열하는 리스트 cost가 
solution 함수의 매개변수로 주어집니다. 
운행가능한 거리가 가장 긴 차량의 이름을 return 하도록 solution 함수를 완성하려 합니다. 
코드가 올바르게 동작할 수 있도록 빈칸을 채워주세요. 
 
매개변수 설명 
홍길동씨가 구매하려고 하는 차량의 이름 리스트 name, 한달동안 차량 운행을 위해 사용할 수 있는 금액 money, 
구매하려고 하는 차량의 연비와 유류비 항목을 나열하는 리스트 cost가 solution 함수의 매개변수로 주어집니다.  
- money는 1,000 이상 500,000 이하입니다. 
- name의 길이는 3 이상 100 이하입니다. 
- cost의 길이는 3 이상 100 이하입니다. 
- cost의 원소는 [연비, 유류비] 형식으로 되어 있습니다. 
연비는 10 이상 100 이하이고, 유류비는 1,000 이상 10,000 이하 입니다. 
유류는 경유와 휘발유 2개의 종류 값만 사용하며, 1달 동안 비용 변동이 없습니다. 
- 이외의 조건은 고려하지 않습니다. 
 
return 값 설명 
운행가능한 거리가 가장 긴 차량의 이름을 return합니다. 
"""

import math

def solution(money, cost, name):
    answer = ""
    max_distance = 0

    i = 0
    while i < len(cost):
        # oil = math.trunc(money / [[quiz]])
        # distance = [[quiz]] * [[quiz]]
        # if distance > [[quiz]]:
        #     max_distance = distance
        #     answer = [[quiz]]
        oil = math.trunc(money / cost[i][1])
        distance = oil * cost[i][0]
        if distance > max_distance:
            max_distance = distance
            answer = name[i]
        i += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
money = 100000
cost = [[50, 5000], [20, 1000], [20, 5000], [50, 1000]]
name = ["A", "B", "C", "D"]
ret = solution(money, cost, name)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")