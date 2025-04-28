# 프로그래머스 81302번: 거리두기 확인하기

def solution(places):
    answer = []
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for place in places:
        flag = True
                
        for i in range(5):
            for j in range(5):
                if not flag:
                    break
                
                if place[i][j] == "P":
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if place[nx][ny] == "O":
                                place[nx] = place[nx][:ny] + "Z" + place[nx][ny + 1:]
                                continue
                                
                            if place[nx][ny] == "P" or place[nx][ny] == "Z":
                                answer.append(0)
                                flag = False                                
                                break
                                
        if flag:
            answer.append(1)
            
    return answer
    
# ----------
# 답안지 보고 보완

def solution(places):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def check_distance(place):
        place = [list(line) for line in place]
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if place[nx][ny] == "P" or place[nx][ny] == "Z":
                                return 0
                            
                            if place[nx][ny] == "O":
                                place[nx][ny] = "Z"
                                continue
        return 1
            
    return [check_distance(place) for place in places]