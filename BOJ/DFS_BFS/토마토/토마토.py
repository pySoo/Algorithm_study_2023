import sys
from collections import deque

day = -1
input = sys.stdin.readline
box = []
ripe = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n = map(int, input().split())
for _ in range(n):
    box.append(list(map(int,input().split())))

def bfs():
  while ripe:
    x, y = ripe.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if box[nx][ny] == 0:
          box[nx][ny] += box[x][y] + 1
          ripe.append([nx,ny])
  

for row in range(n):
  for col in range(m):
    if box[row][col] == 1:
      ripe.append([row,col])

bfs()

for row in range(n):
  max_day = max(box[row]) - 1
  if 0 in box[row]:
    day = -1
    break
  else:
    if max_day > day:
      day = max_day

print(day)