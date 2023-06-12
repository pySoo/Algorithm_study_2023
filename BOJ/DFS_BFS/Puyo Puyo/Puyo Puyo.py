from collections import deque

board = []
answer = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]


for i in range(12):
  board.append(list(input()))

def bfs(i,j,current):
  queue = deque()
  queue.append((i,j))

  popped = deque()
  popped.append((i,j))

  visited = [[False] * 6 for _ in range(12)]
  visited[i][j] = True
  count = 1

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx >= 0 and ny >=0 and nx < 12 and ny < 6:
        if board[nx][ny] == current and not visited[nx][ny]:
          queue.append((nx,ny))
          popped.append((nx,ny))
          visited[nx][ny] = True
          count += 1

  if count >= 4:
    delete_board(popped)
    return 1
  else:
    return 0

def delete_board(popped):
  for x, y in popped:
      board[x][y] = '.'

def down_board():
  for y in range(6):
    next_y = 11
    for x in range(11, -1, -1):
      if board[x][y] != '.':
        board[next_y][y] = board[x][y]
        if next_y != x:
          board[x][y] = '.'
        next_y -= 1
   
while True:
  check = 0
  for i in range(12):
    for j in range(6):
      if board[i][j] != '.':
        check += bfs(i,j,board[i][j])
  if check == 0:
    print(answer)
    break
  else:
    answer += 1
  down_board()