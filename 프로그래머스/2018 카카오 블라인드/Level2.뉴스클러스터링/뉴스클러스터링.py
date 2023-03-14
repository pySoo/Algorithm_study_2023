def find_two_gram(s, list):
    for two_gram in zip(s, s[1:]):
        str = two_gram[0] + two_gram[1]
        if str.isalpha():
            list.append(str.lower())
            
def solution(str1, str2):
    answer = 0
    list_1, list_2 = [], []
    
    find_two_gram(str1, list_1)
    find_two_gram(str2, list_2)
    
    inter = set(list_1) & set(list_2)
    union = set(list_1) | set(list_2)
    
    if len(union) == 0:
        return 65536
    
    inter_sum = sum([min(list_1.count(i), list_2.count(i)) for i in inter])
    union_sum = sum([max(list_1.count(i), list_2.count(i)) for i in union])
    
    return int(inter_sum / union_sum * 65536)