def solution(msg):
    answer = []
    dictionary = {}
    for i in range(1, 27):
        dictionary[chr(i+64)] = i
    # 01 2  
    while msg:
        idx = 0
        
        for i in range(len(msg)):
            if msg[:i+1] in dictionary:
                w = msg[:i+1]
                idx = i
                
        answer.append(dictionary[w])
        msg = msg[idx+1:]
        
        if len(msg) > 0:
            c = msg[0]
            dictionary[w+c] = len(dictionary) + 1
        
                    
    return answer