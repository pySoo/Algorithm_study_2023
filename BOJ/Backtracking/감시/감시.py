import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
cctv = []
for i in range(n):
  row = list(map(int, input().split()))
  board.append(row)
  for j in range(m):
    if row[j] in [1, 2, 3, 4, 5]:
      cctv.append([row[j], i, j])

# 상하좌우
dx = [-1,0,1,0]
dy = [0,1,0,-1]

mode = {
  1: [[0], [1], [2], [3]],
  2: [[0, 2], [1, 3]],
  3: [[0, 1], [1, 2], [2, 3], [0, 3]],
  4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
  5: [[0, 1, 2, 3]],
}

def check_cctv(board, direction, x, y):
  row, col = len(board), len(board[0])
  for i in direction:
    nx, ny = x, y
    while True:
      nx += dx[i]
      ny += dy[i]
      if nx < 0 or ny < 0 or nx >= row or ny >= col:
        break
      if board[nx][ny] == 6:
        break
      elif board[nx][ny] == 0:
        board[nx][ny] = -1
  
def dfs(depth, board):
  global answer
  if depth == len(cctv):
    count = 0
    for i in range(n):
      count += board[i].count(0)
    answer = min(answer, count)
    return

  copy_board = copy.deepcopy(board)
  cctv_num, x, y = cctv[depth]
  for direction in mode[cctv_num]:
    check_cctv(copy_board, direction, x, y)
    dfs(depth+1, copy_board)
    copy_board = copy.deepcopy(board)
    
answer = n * m
dfs(0, board)
print(answer)