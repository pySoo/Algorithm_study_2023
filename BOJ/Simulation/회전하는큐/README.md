## 회전하는 큐 - 1021

[문제 링크](https://www.acmicpc.net/problem/1021)

### 구분

구현, 덱

### 풀이 요약

python의 deque 자료구조를 이용해서 덱 연산을 수행하여 목표 값을 뽑아내는데 필요한 연산의 최소값을 출력하는 문제입니다.

인덱스를 활용하여 왼쪽으로 이동시키는 것과 오른쪽으로 이동시키는 것 중에 더 효율적인 방법을 계산하여 목표 값에 다다를 때까지 이동합니다.

### 나의 풀이

```python
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
targets = list(map(int, input().split()))
temp = list()
for i in range(1, n+1):
    temp.append(i)
queue = deque(temp)

def moveLeft(queue : deque):
    queue.append(queue.popleft())
    return queue

def moveRight(queue : deque):
    queue.appendleft(queue.pop())
    return queue

count = 0

for i in range(m):
    target = targets[i]
    left_move_count = queue.index(target)
    right_move_count = len(queue) - queue.index(target)
    while target != queue[0]:
        if left_move_count < right_move_count:
            for _ in range(left_move_count):
                queue = moveLeft(queue)
                count += 1
        else:
            for _ in range(right_move_count):
                queue = moveRight(queue)
                count += 1
    queue.popleft()

print(count)
```

### 배운 점

deque의 appendLeft라는 연산을 이용해 원소를 맨 앞에 추가할 수 있다는 것을 알게되었습니다. 스택을 이용한 문제에서 popleft() 연산을 이용하기 위해 deque 자료 구조를 많이 사용하기 때문에 deque 활용법에 익숙해지는 것이 필요하다고 생각했는데, 이번 문제에서 deque를 다룰 수 있어서 좋았습니다.

### 문제 설명

지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.

큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

### 입력

첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

### 출력

첫째 줄에 문제의 정답을 출력한다.

### 예제 입력1

```python
10 3
1 2 3
```

### 예제 출력 1
