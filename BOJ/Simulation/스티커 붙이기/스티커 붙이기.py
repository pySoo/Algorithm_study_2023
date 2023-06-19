def rotate(arr):
  arr = zip(*arr[::-1])
  return [list(row) for row in arr]

def compare(x,y,sticker):
  row, col = len(sticker), len(sticker[0])
  for sx in range(row):
    for sy in range(col):
      if board[x+sx][y+sy] == sticker[sx][sy] == 1:
        return False
  return True


def is_attached(sticker):
  row, col = len(sticker), len(sticker[0])

  for x in range(n - row + 1):
    for y in range(m - col + 1):
      if compare(x,y,sticker):
        for sx in range(row):
          for sy in range(col):
            board[x+sx][y+sy] += sticker[sx][sy]
        return True
  return False

n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]

stickers = []

for _ in range(k):
  row, col = map(int, input().split())
  sticker = [list(map(int, input().split())) for _ in range(row)]
  stickers.append(sticker)

for sticker in stickers:
  for i in range(4):
    if is_attached(sticker):
      break
    sticker = rotate(sticker)

answer = sum(map(sum, board))
print(answer)