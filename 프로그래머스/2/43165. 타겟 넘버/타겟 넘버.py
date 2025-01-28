def solution(numbers, target):
    answer = 0
    answers = [0]
    for n in numbers:
        temp = []
        for a in answers:
            temp.append(a + n)
            temp.append(a - n)
        answers = temp
    for a in answers:
        if a == target:
            answer += 1
    return answer