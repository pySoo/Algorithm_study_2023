def solution(array, commands):
    answer = []
    for i, j, k in commands:
        array_list = sorted(array[i-1:j])
        answer.append(array_list[k-1])
    return answer