n = int(input())
signal = input()

col_length = 5
row_length = len(signal) // col_length

board = []

# 문자열을 리스트로 변환하기
for i in range(col_length):
  sliced_row = list(signal[i * row_length : (i+1) * row_length])
  board.append(sliced_row)

# 가장 획이 많은 8을 기준으로 리스트를 만든다.
template = [[] for _ in range(col_length)]

for row in range(3):
  for col in range(col_length):
    if col in [1, 3] and row in [1]:
      template[col].append('.')
    else:
      template[col].append('#')

# 8을 기준으로 없는 부분의 좌표를 저장해서 숫자를 계산한다.
def get_number(board):
  diff = []
  for col in range(col_length):
    for row in range(3):
      if template[col][row] != board[col][row]:
        diff.append([col,row])
  if [0, 1] in diff and [2, 1] in diff and [4, 1] in diff:
    return 1
  elif diff == [[1, 0], [3, 2]]:
    return 2
  elif diff == [[1, 0], [3, 0]]:
    return 3
  elif diff == [[0, 1], [3, 0], [4, 0], [4, 1]]:
    return 4
  elif diff == [[1, 2], [3, 0]]:
    return 5
  elif diff == [[1, 2]]:
    return 6
  elif diff == [[1, 0], [2, 0], [2, 1], [3, 0], [4, 0], [4, 1]]:
    return 7
  elif len(diff) == 0:
    return 8
  elif diff == [[3, 0]]:
    return 9
  else:
    return 0

answer = ''
row = 0

while row < row_length:
  part = [[] for _ in range(col_length)]
  num = 0
  # 만약 가장 윗 열의 글자가 '#'라면 숫자가 시작되는 것이므로 3x5 리스트를 추출한다.
  if board[0][row] == '#':
    for col in range(5):
      part[col].extend(board[col][row : row+3])
      # 끝에 위치한 행이라면 더 추출할 것이 없을 수도 있으므로 '.'로 빈 영역을 채워주어 3x5 리스트를 만든다.
      part[col].extend(['.'] * (3-len(part[col])))
    num = get_number(part)
    answer += str(num)
    # 숫자가 1이라면 1행과 공백을 포함해서 행을 2만큼 증가시킨다.
    if num == 1:
      row += 2
    else:
      row += 4
  else:
    row += 1
    
print(answer)


