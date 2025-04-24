# 프로그래머스 42576번: 완주하지 못한 선수

from collections import Counter

def solution(participant, completion):
#     for name in completion:
#         if name in participant:
#             participant.remove(name)
            
#     return participant[0]

    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    for person in participant:
        if participant_counter.get(person) != completion_counter.get(person):
            return person
        