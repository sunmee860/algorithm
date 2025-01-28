from collections import Counter
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    part_count = Counter(participant)
    comp_count = Counter(completion)
    for p in part_count:
        if part_count[p] != comp_count[p]:
            answer = p
            break
    return answer