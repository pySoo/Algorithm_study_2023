## LCD Test - **2290**

[문제 링크](https://www.acmicpc.net/problem/2290)

### 구분

구현, 문자열

### 풀이 요약

LCD의 패널 영역을 7개로 나눠서 함수를 만들고 각 숫자마다 필요한 영역을 그려서 구현하였다.

숫자별로 함수를 만들어서 구하는 방법도 있었으나, 숫자는 10개이므로 함수 10개가 필요했지만 패널은 7개만 필요하기 때문에 패널을 그리는 방식을 선택했다.

### 나의 풀이

```python
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
```

### 배운 점

와우... 구현 문제는 코드를 정갈하게 작성하려고 해도 한계가 있는 것 같다. 그래도 최대한 함수의 이름과 변수의 이름을 목적에 맞게 정하려고 노력했다.

이번 문제는 LCD 패널을 7개로 나눠서 필요한 부분만 선을 그려주는 방식으로 풀이했다. 이러한 구현 문제는 항상 문제를 작게 분리하여 생각하는게 중요한 것 같다! 처음 마주했을 때는 당황스러울 수 있지만, 0을 어떻게 그리지? 1을 어떻게 그리지? 쪼개서 생각하다보면 아이디어가 나오게 된다. 라인을 그릴 때 문자열 영역이 조금 헷갈렸는데 구현 문제에서는 이런 부분에서 실수하지 않도록 조심해야 할 것 같다. 많이 풀면서 익숙해지도록 해야겠다..

어려운 점이 있었다면 리스트[현재 숫자][행][열] 형태의 3차원 배열로 풀고보니 3차원 리스트를 문자열로 풀어서 출력하는 것이 헷갈렸다. 마지막 숫자를 제외하고 숫자 사이에는 공백이 한 칸 있어야 하기 때문에 마지막 숫자인 경우만 end 옵션을 제거해주었다.

### 문제 설명

지민이는 새로운 컴퓨터를 샀다. 하지만 새로운 컴퓨터에 사은품으로 온 LC-디스플레이 모니터가 잘 안나오는 것이다. 지민이의 친한 친구인 지환이는 지민이의 새로운 모니터를 위해 테스트 할 수 있는 프로그램을 만들기로 하였다.

<h4>입력</h4>
첫째 줄에 두 개의 정수 s와 n이 들어온다. (1 ≤ s ≤ 10, 0 ≤ n ≤ 9,999,999,999)이다. n은 LCD 모니터에 나타내야 할 수 이며, s는 크기이다.

<h4>출력</h4>
길이가 s인 '-'와 '|'를 이용해서 출력해야 한다. 각 숫자는 모두 s+2의 가로와 2s+3의 세로로 이루어 진다. 나머지는 공백으로 채워야 한다. 각 숫자의 사이에는 공백이 한 칸 있어야 한다.

<h4>예제 입력 1</h4>

```
2 1234567890
```

<h4>예제 출력 1</h4>

```
      --   --        --   --   --   --   --   --
   |    |    | |  | |    |       | |  | |  | |  |
   |    |    | |  | |    |       | |  | |  | |  |
      --   --   --   --   --        --   --
   | |       |    |    | |  |    | |  |    | |  |
   | |       |    |    | |  |    | |  |    | |  |
      --   --        --   --        --   --   --
```
