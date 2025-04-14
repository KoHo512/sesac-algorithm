# 프로그래머스 81301번: 숫자 문자열과 영단어
# 강사님 풀이 1

def solution(s):
    numbers = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    
    for key, value in numbers.items():
        s = s.replace(key, value)
            
    return int(s)

# ----------
# 강사님 풀이 2

def solution(s):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for value, key in enumerate(numbers):
        s = s.replace(key, str(value))
    
    return int(s)