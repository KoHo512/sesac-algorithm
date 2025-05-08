# 프로그래머스 42578번: 의상

def solution(clothes):
    closet = {}
    
    for cloth in clothes:
        if cloth[1] in closet:
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]
            
    num_types = list(map(len, closet.values()))
    
    answer = 1
    for type_num in num_types:
        answer *= type_num + 1
        
    return answer - 1

# ----------
# 보완

def solution(clothes):
    closet = {}
    
    for c, t in clothes:
        if t in closet:
            closet[t].append(c)
        else:
            closet[t] = [c]
    
    answer = 1
    for items in closet.values():
        answer *= len(items) + 1
        
    return answer - 1