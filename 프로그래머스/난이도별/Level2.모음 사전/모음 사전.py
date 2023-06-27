def dfs(current, dictionary, alpha_list):
    dictionary.append(current)
    for alpha in alpha_list:
        if len(current) != len(alpha_list):
            dfs(current+alpha, dictionary, alpha_list)
        else:
            current[:-1]
    
def solution(word):
    alpha_list = ['A','E','I','O','U']
    dictionary = []
        
    for i in range(len(alpha_list)):
        dfs(alpha_list[i], dictionary, alpha_list)
    
    return dictionary.index(word) + 1