# DFS 풀이
def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]
    
    def DFS(x):
        visited[x] = True
        for i in range(n):
            if x != i and computers[x][i] == computers[i][x] == 1:
                if not visited[i]:
                    DFS(i)
            
    
    for com in range(n):
        if not visited[com]:
            DFS(com)
            answer += 1
            
    return answer
            
    


# BFS 풀이
from collections import deque

def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]
    
    def BFS(com):
        queue = deque()
        queue.append(com)
        while queue:
            x = queue.popleft()
            visited[x] = True
            for i in range(n):
                if x != i and computers[x][i] == computers[i][x] == 1:
                    if not visited[i]:
                        queue.append(i)
            
    
    for com in range(n):
        if not visited[com]:
            BFS(com)
            answer += 1
            
    return answer
            
    

