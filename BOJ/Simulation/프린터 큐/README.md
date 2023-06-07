## 프린터 큐 - 1966

[문제 링크](https://www.acmicpc.net/problem/1966)

### 구분

구현, 큐(덱)

### 풀이 요약

요구사항에 따라 큐를 조작해서 우선순위에 따라 출력하는 프로그램을 만드는 문제였습니다. 값을 비교하게 되면 동일한 값이 있는 경우 구할 수 없게 되기 때문에 처음부터 (인덱스, 값)의 튜플 구조로 저장해주는 것이 중요한 문제였습니다.

파이썬에서는 덱을 이용하여 popleft()와 append() 연산을 이용하여 구현하였습니다.

### 나의 풀이

```python
from collections import deque

t = int(input())
answer = []
for _ in range(t):
  n, m = map(int, input().split())
  data = deque(map(int,input().split()))
  priority = deque()

  for idx, num in enumerate(data):
    priority.append((idx, num))

  print_num = 0
  while len(priority) > 0:
    idx, front = priority[0]
    max_num = max(priority, key=lambda x: x[1])[1]
    if front >= max_num:
      print_num += 1
      priority.popleft()
      if idx == m:
        break
    else:
      priority.popleft()
      priority.append((idx, front))

  answer.append(print_num)

for num in answer:
  print(num)
```

### 배운 점

파이썬에서 튜플의 max 값을 구하는 방법을 배울 수 있었습니다.

```python
max_num = max(priority, key=lambda x: x[1])[1]
```

sort 함수와 비슷하게 key를 이용하면 튜플의 특정 값을 기준으로 max 값을 구할 수 있습니다. 저는 여기서 숫자만 가져오는게 필요했기 때문에 [1]를 이용해서 인덱스가 아닌 숫자만 가져오도록 했습니다.

### 문제 설명

여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

### 입력

첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

### 출력

각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

### 예제 입력1

```
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
```

### 예제 출력 1

```
1
2
5
```
