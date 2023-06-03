from collections import deque

n = int(input())
board = []
dx, dy = [1,-1,0,0], [0,0,1,-1]
town = []
count = 0

for _ in range(n):
  board.append(list(map(int, input())))

def bfs(i,j):
  global count
  count = 1
  q = deque()
  q.append([i,j])
  board[i][j] = -1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < n:
        if board[nx][ny] == 1:
          q.append([nx,ny])
          count += 1
          board[nx][ny] = -1
        
def dfs(x,y):
  global count
  board[x][y] = -1
  count += 1
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
      if board[nx][ny] == 1:
        dfs(nx, ny)
  

for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      # dfs(i,j)
      bfs(i,j)
      town.append(count)
      count = 0
    
town.sort()
print(len(town))

for i in range(len(town)):
  print(town[i])