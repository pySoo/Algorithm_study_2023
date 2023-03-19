def solution(id_list, report, k):
    answer = [0] * len(id_list)
    ban_dict = {id: [] for id in id_list}
    
    report = set(report)
    
    for r in report:
        reporter, banned = r.split()
        ban_dict[banned].append(reporter)
    
    for banned, reporters in ban_dict.items():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[id_list.index(reporter)] += 1
            
    return answer