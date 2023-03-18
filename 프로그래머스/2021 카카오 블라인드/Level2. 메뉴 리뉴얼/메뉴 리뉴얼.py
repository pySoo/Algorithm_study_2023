from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for course_num in course:
        arr = []
        for order in orders:
            combi = combinations(sorted(order), course_num)
            arr.extend(list(combi))
        
        counter = Counter(arr)
        
        if len(counter) != 0 and max(counter.values()) != 1:
            max_value = max(counter.values())
            for key in counter:
                if counter[key] == max_value:
                    answer.append(''.join(key))
            
    return sorted(answer)