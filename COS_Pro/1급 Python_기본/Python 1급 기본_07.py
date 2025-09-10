"""
주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 solution 함수와 
func1, func2, func3에서 잘못된 부분 한 줄을 수정해주세요. 
ㅇㅇ도시락 업체에서는 ‘A’선수가 소속된 ㅁㅁ탁구팀의 점심도시락 준비를 주문받았습니다. 
하지만 탁구팀의 인원수를 적어놓은 주문서가 손상되어 알아볼 수 없게 되어버렸습니다. 
대신 ㅁㅁ탁구팀이 연습하고 있는 체육관의 연습경기 대진표를 입수하게 되었는데, 
이 대진표로 ㅁㅁ탁구팀의 팀원이 총 몇 명인지 유추하려고 합니다. 
연습 중인 체육관에는 총 2개의 탁구팀이 연습중입니다. 
대진표에는 2개의 탁구팀의 경기가 뒤섞여 있지만, 경기는 같은 팀원들끼리만 하도록 구성되어 있습니다. 
그래서 다른 탁구팀의 인원까지 카운트하지 않도록 ‘A’선수가 소속된 ㅁㅁ탁구팀의 팀원만 카운트해야합니다.  
예를 들어 A와 B가 경기하고, B와 C가 경기하고, D와 E가 경기하고, C와 F가 경기한다면 
A선수와 같은 탁구 팀원은 A, B, C, F로 총 4명입니다. 
연습경기 대진표가 담긴 배열 list가 solution함수의 매개변수로 주어질 때, 
점심도시락을 몇 개 준비하면 될지 ㅁㅁ탁구팀의 팀원의 수를 올바르게 return하세요. 
 
매개변수 설명 
연습경기 대진표가 담긴 리스트 list가 solution 함수의 매개변수로 주어집니다. 
- list의 원소는 같은 팀인 두 사람의 이름입니다. 
- 두 사람의 이름은 각각 한 글자 대문자 알파벳입니다. 
- X,Y 두 사람을 예로 들면 X의 이름은 항상 Y의 이름보다 사전 순으로 앞섭니다. 
- X,Y 두 사람을 예로 들면 list는 X의 이름을 기준으로 정렬되어 있습니다. 
- list의 길이는 3 이상 10 이하입니다. 
 
return 값 설명 
"A"와 같은 탁구 팀원의 인원수를 return 해주세요.
"""

ALPHANUM = 26


def func1(number, arr1, arr2):
    arr2[number] = True
    for i in range(ALPHANUM):
        if arr1[number][i] and not arr2[i]:
            func1(i, arr1, arr2)

def func2(arr):
    answer = 0
    for value in arr:
        # if not value:
        if value:
            answer += 1
    return answer

def func3(arr1, arr2):
    for elem1, elem2 in arr1:
        num1, num2 = ord(elem1) - ord('A'), ord(elem2) - ord('A')
        arr2[num1][num2] = True
        arr2[num2][num1] = True


def solution(list):
    graph = [[False for _ in range(ALPHANUM)] for _ in range(ALPHANUM)]
    visited = [False] * ALPHANUM

    func3(list, graph)
    visited[0] = True
    for node in range(ALPHANUM):
        if graph[0][node] and not visited[node]:
            func1(node, graph, visited)
    return func2(visited)

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
list = ["AB", "BC", "DE", "CF"]
ret = solution(list)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")