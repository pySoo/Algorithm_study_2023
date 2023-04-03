from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    queue = deque()
    queue.append((0,0))
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        
        if x == n-1 and y == m-1:
            return maps[n-1][m-1]
        
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    maps[nx][ny] = maps[x][y] + 1
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    
    return -1