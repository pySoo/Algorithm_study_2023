def solution(new_id):
    answer = new_id
    #1
    answer = answer.lower()
    #2
    tmp = ''
    for s in answer:
        if s.isalnum() or s in '-_.':
            tmp += s
    answer = tmp
    
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    #4
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    #5
    if answer == '':
        answer = 'a'
    
    #6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #7
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))

    return answer