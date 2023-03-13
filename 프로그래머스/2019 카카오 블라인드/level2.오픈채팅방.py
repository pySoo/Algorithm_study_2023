def solution(record):
    answer = []
    user_dic = {}
    
    for sentence in record:
        sentence_splited = sentence.split()
        if len(sentence_splited) == 3:
            user_dic[sentence_splited[1]] = sentence_splited[2]
            
    for sentence in record:
        sentence_splited = sentence.split()
        if sentence_splited[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %user_dic[sentence_splited[1]])
        elif sentence_splited[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %user_dic[sentence_splited[1]])
            
    return(answer)
