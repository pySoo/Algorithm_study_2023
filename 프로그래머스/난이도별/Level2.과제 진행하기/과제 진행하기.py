def convert_time_to_number(prev, start):
    prev = list(map(int, prev.split(':')))
    start = list(map(int, start.split(':')))
    return (start[0] - prev[0]) * 60 + start[1] - prev[1]

def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])
    doing = [plans.pop(0)]
    
    for plan in plans:
        name, start, playtime = plan
        if doing:
            prev_name, prev_start, prev_playtime = doing[-1]
            prev_playtime = int(prev_playtime)
            passed_time = convert_time_to_number(prev_start, start)
        
            if passed_time == prev_playtime:
                doing.pop()
                answer.append(prev_name)
            elif passed_time > prev_playtime:
                while doing:
                    prev_name, prev_start, prev_playtime = doing[-1]
                    prev_playtime = int(prev_playtime)
                    
                    if passed_time >= prev_playtime:
                        doing.pop()
                        answer.append(prev_name)
                        passed_time -= prev_playtime
                    else:
                        doing[-1] = [prev_name, prev_start, prev_playtime - passed_time]
                        break
            elif passed_time < prev_playtime:
                doing[-1] = [prev_name, prev_start, prev_playtime - passed_time]
            
        doing.append(plan)
    
    while doing:
        answer.append(doing.pop()[0])
        
    return answer