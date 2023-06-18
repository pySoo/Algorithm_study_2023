from itertools import combinations
from collections import defaultdict

def get_dict(s):
    dicts = defaultdict(int)
    for i in range(len(s)-1):
        element = s[i:i+2]
        if element.isalpha():
            dicts[element] += 1
    return dicts
    
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    dict1, dict2 = get_dict(str1), get_dict(str2)
    
    intersect = defaultdict()
    union = dict2
    
    for key, value in dict1.items():
        if key in dict2:
            intersect[key] = min(value, dict2[key])
            union[key] = max(value, dict2[key])
        else:
            union[key] = value
    
    if len(union) == 0:
        return 65536
    return int(sum(intersect.values()) / sum(union.values()) * 65536)
        