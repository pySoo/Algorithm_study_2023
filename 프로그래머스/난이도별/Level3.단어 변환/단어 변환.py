from collections import deque
def checkDiffWord(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False
    

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        a, cnt = queue.popleft()
        if a == target:
            return cnt
        
        for i in range(len(words)):
            b = words[i]
            if checkDiffWord(a, b):
                queue.append((b, cnt+1))
    
    return 0