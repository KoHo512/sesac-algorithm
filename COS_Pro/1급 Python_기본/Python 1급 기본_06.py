"""
게임 아이템의 이동 값을 계산하는 알고리즘을 구하려 합니다. 
x축을 기준으로 좌우로 이동할 수 있는 캐릭터는 특정한 위치에 놓여 있는 아이템을 모두 얻기 위해 이동해야 합니다. 
캐릭터의 처음 위치가 주어졌을 때 모든 아이템을 얻기 위해 캐릭터의 최소 이동 값을 구하려 합니다. 
캐릭터의 처음 위치 start와 각 아이템의 위치 정보를 담은 배열 locations이 solution 함수의 매개변수로 주어질 때, 
캐릭터의 최소 이동 값을 return 하도록 solution 함수를 작성했습니다. 
그러나, 코드 일부분이 잘못 되어있기 때문에 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 
주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.  

매개변수 설명 
캐릭터의 처음 위치 start와 각 아이템의 위치 정보를 담은 배열 locations가 solution 함수의 매개변수로 주어집니다. 
- locations의 길이는 1 이상 100 이하입니다. 
- locations의 원소는 1 보다 크고 100 보다 작거나 같은 자연수입니다. 
- start는 1 보다 크고 100 보다 작거나 같은 자연수입니다. 

return 설명 
캐릭터의 최소 이동 값을 return 해주세요. 
"""

def solution(start, locations):
    answer = 0
    # min = 0
    min = float("INF")      # 100
    max = 0
    for i in locations:
        if i < min:
            min = i
        if i > max:
            max = i
            
    if start <= min:
        answer = max - start
    elif start >= max:
        answer = start - min
    else:
        if start - min < max - start:
            answer = start - min + (max - min)
        else:
            answer = max - start + (max - min)
            
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
start = 15
locations = [10, 62, 22]
ret = solution(start, locations)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")