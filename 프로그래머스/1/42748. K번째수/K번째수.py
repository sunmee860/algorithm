def solution(array, commands):
    answer = []
    for i,j,k in commands:
        answers = array[i-1:j]
        answers.sort()
        answer.append(answers[k-1])
    return answer