## 단지 번호 붙이기 - 2667

[문제 링크](https://www.acmicpc.net/problem/2667)

### 구분

그래프 탐색, DFS, BFS

### 풀이 요약

DFS/BFS의 대표 유형이라고 할 수 있는 문제였습니다. 배열을 벗어나는 케이스에 대한 예외 처리를 해주고 방문한 곳은 값을 바꾼 다음 count 값을 높여주는 방식으로 풀이했습니다.

### 나의 풀이

```python
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
      dfs(i,j)
      # bfs(i,j)
      town.append(count)
      count = 0

town.sort()
print(len(town))

for i in range(len(town)):
  print(town[i])
```

### 배운 점

DFS와 BFS 코드를 모두 작성해보면서 그래프 유형에 대한 감을 다시 익힐 수 있었습니다. 더불어 python의 global 키워드 사용법에 대해 배울 수 있었습니다. python에서는 전역 변수의 값을 특정 함수 안에서 변경할 때 global 키워드를 사용해야 합니다. 만약 global 키워드를 사용하지 않고 값을 변경하는 경우, 함수 안에서의 새로운 지역 변수가 선언됩니다.

DFS/BFS의 대표 유형 문제를 풀어보았기 때문에 둘의 차이점에 대해서 간단하게 정리해보고자 합니다.

### DFS

- 탐색 방법: 현재 정점에서 갈 수 있는 점들까지 깊이 들어가면서 탐색 **(모든 경우의 수 탐색)**
- 구현 방법: 스택 또는 **재귀 함수**로 구현
- 어떤 문제에 적용하나요?: 모든 정점 방문이 필요하다면 추천

### BFS

- 탐색 방법: 현재 정점에 연결된 **가까운 점들부터 탐색**
- 구현 방법: 큐를 이용해서 구현
- 어떤 문제에 적용하나요?: **최단 거리**를 구해야 한다면 추천

### 문제 설명

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

### 입력

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

### 출력

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

### 예제 입력 1

```
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```

### 예제 출력 1

```
3
7
8
9
```
