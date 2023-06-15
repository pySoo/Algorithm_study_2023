from collections import defaultdict

def solution(N, stages):
    answer = defaultdict(int)
    stages.sort()
    
    not_clear = 0
    in_stage = len(stages)
    
    for level in range(1, N+1):
        not_clear = 0
        for i in range(len(stages)):
            stage = stages[i]
            if stage == level:
                not_clear += 1
            elif stage > level:
                answer[level] = not_clear / in_stage
                in_stage -= not_clear
                break
        if level not in answer:
            answer[level] = not_clear / in_stage
    
    return sorted(answer, key=lambda x: answer[x], reverse=True)