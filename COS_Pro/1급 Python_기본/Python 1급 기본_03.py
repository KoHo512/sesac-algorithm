"""
모둠 발표 순서를 정하려 합니다. 발표 순서를 정하는 기준은 아래와 같습니다. 
- 프로젝트 설계 점수가 높은 모둠이 먼저 발표합니다. 
- 프로젝트 설계 점수가 같으면 프로젝트 구현 점수가 높은 모둠이 먼저 발표합니다. 
- 프로젝트 설계 점수와 프로젝트 구현 점수가 같으면 모둠 번호가 작은 모둠이 먼저 발표합니다. 
모둠 번호, 프로젝트 설계 점수, 프로젝트 구현 점수를 담은 2차원 리스트 projects가 solution 함수의 매개변수로 주어집니다. 
기준에 따라 발표할 순서대로 모둠 번호를 나열한 리스트를 return 하도록 solution 함수를 작성하려 합니다. 
빈칸을 채워 전체 코드를 완성해주세요. 
 
매개변수 설명 
모둠 번호, 프로젝트 설계 점수, 프로젝트 구현 점수를 담은 2차원 리스트 projects가 solution 함수의 매개변수로 주어집니다. 
- projects의 길이는 3 이상 1,000 이하입니다. 
- projects의 원소는 [모둠 번호, 프로젝트 설계 점수, 프로젝트 구현 점수] 형식입니다. 
- 모둠 번호는 1 이상 1,000 이하인 자연수입니다. 
- 모둠 번호가 같은 경우는 없습니다.  
- 프로젝트 설계 점수와 프로젝트 구현 점수는 1 이상 100 이하인 자연수입니다. 
 
return 설명 
기준에 따라 발표할 순서대로 모둠 번호를 나열한 리스트를 return 합니다. 
"""

def solution(projects):
    # projects.sort(key=lambda x: x[0], [[quiz]])
    # projects.sort(key=lambda x: x[2], [[quiz]])
    # projects.sort(key=lambda x: x[1], [[quiz]])
    # answer = [[quiz]]
    projects.sort(key=lambda x: x[0], reverse=False)
    projects.sort(key=lambda x: x[2], reverse=True)
    projects.sort(key=lambda x: x[1], reverse=True)
    answer = [project[0] for project in projects]
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
projects = [[5, 90, 90], [1, 90, 70], [3, 95, 70], [2, 85, 85], [4, 70, 90]]
ret = solution(projects)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")