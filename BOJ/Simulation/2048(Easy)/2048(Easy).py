from collections import deque
import copy

n = int(input())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move_block(board, length):
  shifted_list = []
  for row in board:
    shifted_queue = deque([x for x in row if x != 0])
    queue = deque()
    prev = 0

    while shifted_queue:
      x = shifted_queue[0]
      if prev == x:
        queue.append(x * 2)
        shifted_queue.popleft()
        prev = 0
      else:
        if prev != 0:
          queue.append(prev)
        prev = shifted_queue.popleft()
    if prev != 0:
      queue.append(prev)

    while len(queue) != length:
      queue.append(0)
    shifted_list.append(list(queue))
  return shifted_list


def forward_90(board):
  n, m = len(board), len(board[0])
  temp = [[0] * n for _ in range(m)]
  for c in range(m):
    for r in range(n):
      temp[c][r] = board[n - 1 - r][c]
  return temp


def back_90(board):
  n, m = len(board), len(board[0])
  temp = [[0] * n for _ in range(m)]
  for c in range(m):
    for r in range(n):
      temp[c][r] = board[r][m - 1 - c]
  return temp


def dfs(n, board):
  global answer
  if n == 5:
    for i in range(len(board)):
      for j in range(len(board)):
        if board[i][j] > answer:
          answer = board[i][j]
    return

  for i in range(4):
    rotated = copy.deepcopy(board)
    for j in range(i):
      rotated = forward_90(rotated)
    rotated = move_block(rotated, len(board))
    for j in range(i):
      rotated = back_90(rotated)
    dfs(n + 1, rotated)


answer = 0
dfs(0, board)
print(answer)