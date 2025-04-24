# 프로그래머스 1845번: 폰켓몬

def solution(nums):
    nums_set = set(nums)
    
    return min(len(nums_set), len(nums) / 2)