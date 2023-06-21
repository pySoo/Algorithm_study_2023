## 2048(Easy) - 12100

[문제 링크](https://www.acmicpc.net/problem/12100)

### 구분

구현, 브루트포스

### 풀이 요약

**dfs를 이용하여 5번 움직이는 모든 경우의 수를 탐색**하고, 2차원 형태의 게임판을 **상하좌우로 기울였을 때**의 형태를 구현하는 문제였습니다.

게임판을 기울이는 로직을 만드는 것이 어려웠지만.. 단계를 잘게 쪼개서 생각하다보면 답이 나온다는 것을 느꼈던 문제였습니다. 가장 쉽게 생각할 수 있는 상황인 배열을 왼쪽으로 기울였을 때를 먼저 구현하고, 이 방법을 상하우에 어떻게 적용할 수 있을지 생각해보면 됩니다.

### 게임판을 기울이는 방법

**게임판을 왼쪽으로 기울인 모습**을 구현하는 방법입니다.

1. 2차원 배열의 한 행마다 deque 자료구조로 만들고 0이 아닌 원소만 남겨둡니다.
2. 숫자를 합친 결과를 담을 새로운 deque을 생성합니다.
3. 만약 1번 deque의 맨 앞의 원소가 이전 값과 같다면, 새로운 deque에 둘을 더한 값을 넣어줍니다.
4. 맨 앞 원소가 이전 값과 같지 않다면, 새로운 deque에 이전 값을 넣어줍니다.
5. 원래 배열의 길이만큼 0을 추가해줍니다.

사실 방향별로 if문을 주어서 다르게 구현해도 되지만, 기하학적 아이디어를 떠올리면 같은 코드로 처리할 수 있는 방법이 있습니다.

<img width="350px" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FKJJbp%2FbtqFJbBKQic%2FqVzPdLCKTfQeHn5vxHnDWk%2Fimg.png" />

지금까지의 풀이는 첫 번째 사각형에서 L쪽으로 기울이는 코드를 가지고 있는데, D쪽으로 기울이고 싶다면 두 번째 사각형과 같이 보드를 시계 방향으로 90도를 회전하고 똑같이 왼쪽으로 기울이면 처리할 수 있게 됩니다.

여기서 주의할 점은 회전한 만큼 다시 반시계 방향으로 돌려주어야 합니다.

**상하좌우로 기울이는 방법**

1. 좌하우상 순서에 따라 각 시계방향으로 0도, 90도, 180도, 270도로 배열을 회전시켜줍니다. (사진 참고) (forward_90)
2. 게임판을 왼쪽으로 기울였을 때의 처리를 해줍니다. (move_block)
3. 게임판을 다시 반시계 방향으로 돌려줍니다. (back_90)

### dfs를 이용하여 5번 기울이는 모든 경우 구하기

1. 현재 보드와 재귀 횟수를 파라미터로 갖는 dfs 함수를 선언합니다.
2. 재귀 횟수가 5가 되었을 때, 보드에서 가장 큰 값을 정답으로 설정합니다.
3. 4개의 방향별로 재귀 횟수+1과 이동시킨 배열을 넘겨주도록 dfs 재귀를 반복합니다.

### 나의 풀이

```python
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
```

### 배운 점

배열을 시계 방향, 반시계 방향으로 회전시키는 방법을 배울 수 있었습니다. zip을 사용하면 가장 편리하지만, 인덱스 별로 접근해서 회전시키는 방법을 알아두면 배열을 다루는 것에 더 익숙해질 것 같아서 반복문을 활용해보았습니다.

```python
"""
시계 방향 90도 회전
board[x][y] = board[y][row-1-x]

3x4 -> 4x3
(0,0) -> (0,2)
(1,1) -> (1,1)
(2,2) -> (2,0)
(0,3) -> (3,3)

1 0 0 0     0 0 1
0 2 0 0  -> 0 2 0
0 0 3 0     3 0 0
						0 0 0
"""
for row in range(m):
	for col in range(n):
		temp[row][col] = board[col][n-1-row]

# zip 이용 풀이
list(map(list, zip(*arr[::-1])))
```

```python
"""
반시계 방향 90도 회전
board[x][y] = board[col-1-y][x]

시계 방향에서 x,y 로직만 반대로 바꿔주면 됩니다.
"""
for row in range(m):
	for col in range(n):
		temp[row][col] = board[m-1-col][row]

# zip 이용 풀이
list(map(list, zip(*arr)))[::-1]
```

배열을 회전시키는 구현 문제에 취약한 것 같아서 이번 문제를 풀어보았습니다. 이해에만 몇 시간을 쓴만큼 어렵게 느꼈던 문제지만,, 이렇게 정리를 해두면 다음에 비슷한 유형을 만났을 때 조금 더 수월하게 방법을 떠올릴 수 있지 않을까 생각합니다. 부스트 캠프 2차 시험도 제발 꼭 통과했으면 좋겠습니다. 😭 2일의 노력으로 앞으로 6개월의 인생이 달라질 수 있다 생각하고 마음을 다잡고 구현 문제들을 열심히 풀어봐야겠습니다.

### 문제 설명

2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 [링크](https://gabrielecirulli.github.io/2048/)를 누르면 게임을 해볼 수 있다.

이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다. 이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다. 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다. (실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)

이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

### 입력

첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

### 출력

최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.

### 예제 입력1

```
3
2 2 2
4 4 4
8 8 8
```

### 예제 출력 1

```
16
```
