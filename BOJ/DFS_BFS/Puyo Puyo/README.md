## Puyo Puyo - 11559

[문제 링크](https://www.acmicpc.net/problem/11559)

### 구분

구현, BFS

### 풀이 요약

상하좌우로 같은 원소를 찾아서 제거해주는게 필요하기 때문에 BFS를 사용하면 풀이할 수 있는 구현 문제였습니다.

풀이 과정은 다음과 같습니다.

1. board를 돌면서 '.'이 아닌 것(뿌요)을 발견하면 BFS를 실행한다.

2. BFS로 진입하여 4개 이상 연결된 뿌요를 모두 터뜨려 준다. (delete_board)

3. 뿌요가 터졌기 때문에 중력에 따라 board를 아래로 내려준다. (down_board)

4. 터뜨릴 수 있는 뿌요가 계속 남아있을 때 까지 위 과정을 반복한다.

### 나의 풀이

```python
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
    for x in range(10, -1, -1):
      for next_x in range(11, x, -1):
        if board[x][y] != "." and board[next_x][y] == ".":
          board[next_x][y] = board[x][y]
          board[x][y] = "."

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
```

### 배운 점

bfs를 이용해서 원소들을 삭제하고 y축으로 내려주는 방법에 대해서 배울 수 있었습니다. 이전에도 카카오 기출 문제에서 비슷한 유형을 풀어봤던 것 같은데, 다시 풀어봐도 쉽지 않은 유형인 것 같습니다. 따라서 이번에 코드에 주석을 달아서 원리를 이해하고 방법을 기억하고자 합니다.

```Python
def down_board():
  for y in range(6):
    # 가장 밑의 행보다 1만큼 큰 범위에서 진행합니다. (적어도 1칸은 내려주어야 하므로)
    for x in range(10, -1, -1):
      # 1칸만 내려가는게 아닐 수 있으므로 가장 아래의 행을 기준으로 진행합니다.
      for next_x in range(11, x, -1):
        # 만약 현재 행의 원소가 뿌요고 다음 행의 원소가 비어있다면, 해당 뿌요를 다음 행으로 내려줍니다. 그리고 현재의 행의 원소는 비워줍니다.
        if board[x][y] != "." and board[next_x][y] == ".":
          board[next_x][y] = board[x][y]
          board[x][y] = "."
```

마지막으로 헷갈렸던 점은 bfs에서 count를 어느 범위에서 해주어야 하는지 였습니다. 만약 뿌요를 터트릴 때마다 count를 해준다면, 두 뿌요가 터지는 경우에도 두 개를 카운트를 해 주므로 bfs 함수가 아닌 바깥 영역에서 count를 해주어야 했습니다.

이번 문제와 같이 중복 count를 하면 안 되는 문제의 경우 bfs 바깥 영역에서 count를 하는 방식을 떠올려 봐야겠습니다.

### 문제 설명

뿌요뿌요의 룰은 다음과 같다.

필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.

뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.

뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.

아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.

터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

남규는 최근 뿌요뿌요 게임에 푹 빠졌다. 이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다. 하지만 아직 실력이 부족하여 남규는 자기 필드에만 신경 쓰기 바쁘다. 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!

### 입력

총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.

이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.

R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.

입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.

### 출력

현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.

### 예제 입력1

```
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.
```

### 예제 출력 1

```
3
```
