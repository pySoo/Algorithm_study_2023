"""
s=글자 크기, n=모니터에 나타낼 수
가로: s+2 세로: 2s+3

LCD를 7개의 영역으로 분리

1: 맨 위
2: 왼쪽 위
3: 오른쪽 위
4: 가운데
5: 왼쪽 아래
6: 오른쪽 아래
7: 맨 아래

"""

s, n = input().split()
s = int(s)

guide = {'0': [1,2,3,5,6,7], '1': [3,6], '2': [1,3,4,5,7], '3': [1,3,4,6,7], '4':[2,3,4,6], '5':[1,2,4,6,7], '6': [1,2,4,5,6,7], '7' : [1,3,6], '8' : [1,2,3,4,5,6,7], '9': [1,2,3,4,6,7]}

answer = [[[' ' for _ in range(s+2)] for _ in range(2*s+3)] for _ in range(len(n))]

row = '-'
col = '|'

def top(panel):
  for i in range(1, s+1):
    panel[0][i] = row

def lt(panel):
  for i in range(1, s+1):
    panel[i][0] = col

def rt(panel):
  for i in range(1, s+1):
    panel[i][-1] = col

def md(panel):
  for i in range(1, s+1):
    panel[s+1][i] = row

def bl(panel):
  for i in range(s+2, 2*s+2):
    panel[i][0] = col

def rl(panel):
  for i in range(s+2, 2*s+2):
    panel[i][-1] = col

def bottom(panel):
  for i in range(1, s+1):
    panel[2*s+2][i] = row

def draw(num, panel):
  guide_arr = guide[num]
  for n in guide_arr:
    if n == 1:
      top(panel)
    elif n == 2:
      lt(panel)
    elif n == 3:
      rt(panel)
    elif n == 4:
      md(panel)
    elif n == 5:
      bl(panel)
    elif n == 6:
      rl(panel)
    elif n == 7:
      bottom(panel)

for i, num in enumerate(n):
  draw(num, answer[i])

for col in range(2 * s + 3):
  for num_idx in range(len(n)):
    if num_idx == len(n) - 1:
      print(''.join(answer[num_idx][col]))
    else:
      print(''.join(answer[num_idx][col]), end=' ')