## 거북이 - 8911

[문제 링크](https://www.acmicpc.net/problem/8911)

### 구분

구현

### 풀이 요약

x, y 좌표 내에서 동서남북으로 이동한 경로를 저장하고, 경로를 이어서 만들 수 있는 가장 큰 직사각형의 넓이를 구하는 문제였습니다.

시계 방향 또는 반시계 방향으로 방향을 바꾸는 요구사항이 있어서, 시계 방향 기준으로 방향의 좌표를 배열로 저장하여 풀이했습니다.

넓이를 구하는 과정에서 살짝 헤맸는데, 각 x,y 좌표의 최소와 최대를 구하고 그 둘의 절대값을 곱하는 방식으로 풀이했습니다.

### 나의 풀이

```python
t = int(input())

# 북, 동, 남, 서 (x, y)
directions = [[0,1], [1,0], [0,-1], [-1,0]]

def calculate_y(command, pos, dir):
  if command == 'F':
    return [a + b for a, b in zip(pos, dir)]
  elif command == 'B':
    return [a - b for a, b in zip(pos, dir)]

def calculate_x(command, dir):
  if command == 'L':
    next_idx = (directions.index(dir) + 1) % len(directions)
    return directions[next_idx]
  elif command == 'R':
    next_idx = (directions.index(dir) - 1 + len(directions)) % len(directions)
    return directions[next_idx]

def go_turtle(command_list):
  positions = []

  current_dir = directions[0]
  current_pos = [0,0]
  positions.append(current_pos)

  for command in command_list:
    if command == 'F' or command == 'B':
      current_pos = calculate_y(command, current_pos, current_dir)
      positions.append(current_pos)

    elif command == 'L' or command == 'R':
      current_dir = calculate_x(command, current_dir)

  max_x, max_y = 0, 0
  min_x, min_y = 0, 0

  for x,y in positions:
    max_x, max_y = max(max_x, x), max(max_y, y)
    min_x, min_y = min(min_x, x), min(min_y, y)

  height = abs(max_y) + abs(min_y)
  width = abs(max_x) + abs(min_x)
  print(height * width)

for _ in range(t):
  go_turtle(list(input()))
```

### 배운 점

구현 문제에서 최대 넓이를 구하는 문제가 충분히 나올 수 있을 것 같아서 이 문제로 연습해보길 다행이라는 생각이 들었습니다.
넓이를 구하는 방법은 x, y좌표의 최대 최소 값을 구해서 그 둘의 절대값(길이)을 더하는 것이 적절한 풀이 방법이었습니다. 첫 시도에서는 둘을 더하지 않고 max 값만 구했었는데 점과 점을 이어야 선분이 된다는 것을 생각해두면 잊지 않을 수 있을 것 같습니다.

### 문제 설명

상근이는 2차원 평면 위에서 움직일 수 있는 거북이 로봇을 하나 가지고 있다. 거북이 로봇에게 내릴 수 있는 명령은 다음과 같이 네가지가 있다.

F: 한 눈금 앞으로
B: 한 눈금 뒤로
L: 왼쪽으로 90도 회전
R: 오른쪽으로 90도 회전
L과 R명령을 내렸을 때, 로봇은 이동하지 않고, 방향만 바꾼다. 명령을 나열한 것을 거북이 로봇의 컨트롤 프로그램이라고 한다.

상근이는 자신의 컨트롤 프로그램으로 거북이가 이동한 영역을 계산해보려고 한다. 거북이는 항상 x축과 y축에 평행한 방향으로만 이동한다. 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이를 구하는 프로그램을 작성하시오. 단, 직사각형의 모든 변은 x축이나 y축에 평행이어야 한다.

아래 그림에서 거북이는 가장 처음에 (0, 0)에 있고, 북쪽을 쳐다보고 있다. 컨트롤 프로그램이 FLFRFLBRBLB인 경우에 거북이는 아래와 같이 움직인다. 회색으로 빗금친 부분이 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형이다. 넓이는 4가 된다.

거북이가 지나간 영역이 직사각형을 만들지 않는 경우도 있다. 예를 들어, FFLLFF인 경우에 거북이는 y축의 위로만 지나다닌다. 이 경우에 거북이가 지나간 영역을 모두 포함하는 직사각형은 선분이고, 선분은 한 변이 0인 직사각형으로 생각할 수 있다. 따라서, 선분의 경우에 넓이는 0이 된다.

### 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 컨트롤 프로그램이 주어진다. 프로그램은 항상 문제의 설명에 나와있는 네가지 명령으로만 이루어져 있고, 길이는 500을 넘지 않는다.

### 출력

각 테스트 케이스에 대해서, 거북이가 이동한 영역을 모두 포함하는 가장 작은 직사각형의 넓이를 출력한다.

### 예제 입력1

```
3
FFLF
FFRRFF
FFFBBBRFFFBBB
```

### 예제 출력 1

```
2
0
9
```
