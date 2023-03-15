from itertools import combinations

def solution(relation):
    col = len(relation[0])

    candidate_keys = []
    
    #가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
    
    for comb in combi:
        hist = []
        for row in relation:
            current_key = [row[c] for c in comb]
            
            # 하나라도 중복되는 경우: 식별 불가능 
            if current_key in hist:
                break
            else:
                hist.append(current_key)
            # 하나도 중복 안 된 경우: 식별 가능
        else:
            for candidate_key in candidate_keys:
                # 최소성 확인 
                if set(candidate_key).issubset(set(comb)):
                    break
            else:
                candidate_keys.append(comb)
                    
    return len(candidate_keys)
