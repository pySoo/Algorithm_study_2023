from collections import defaultdict

def check_keys(key, query_list):
    key_list = key.split(',')
    
    cnt = 0
    for key in key_list:
        if key in query_list:
            cnt += 1
    
    return len(query_list) == cnt


def check_score(values, score):
    start, end = 0, len(values) - 1
    
    if values[-1] < score:
        return 0
    
    while start < end:
        mid = (start + end) // 2
        if values[mid] >= score:
            end = mid
        else:
            start = mid + 1
    
    return len(values) - end
    
    
    
def solution(info, query):
    answer = []
    applicants = defaultdict(list)
    
    for command in info:
        command = command.split()
        score = int(command[-1])
        parsed_command = ','.join(command[:-1])
        applicants[parsed_command].append(score)
    
    for key in applicants:
        applicants[key].sort()
    
    for command in query:
        command_list = command.replace('and','').split()
        score = int(command_list[-1])
        
        command_list = [x for x in command_list if x != '-'][:-1]
        
        applicant = 0
        for key, values in applicants.items():
            if check_keys(key, command_list):
                applicant += check_score(values, score)
                
        answer.append(applicant)
        
    return answer