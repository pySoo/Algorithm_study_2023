## 집합 - 11723

[문제 링크](https://www.acmicpc.net/problem/11723)

### 구분

구현, 집합

### 풀이 요약

요구사항대로 주어진 명령어에 따라 집합 연산을 수행하면 되는 문제였습니다.
input의 길이가 항상 같지 않기 때문에 command만 주어진 경우 예외 처리를 해주는 것이 필요했습니다.

### 나의 풀이

```Python
import sys
input = sys.stdin.readline

s = set()
n = int(input())

for _ in range(n):
    tmp = input().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue
    command, target = tmp[0], tmp[1]
    target = int(target)

    if command == 'add':
        s.add(target)
    elif command == 'check':
        print(1 if target in s else 0)
    elif command == 'remove':
        s.discard(target)
    elif command == 'toggle':
        if target in s:
            s.discard(target)
        else:
            s.add(target)
```

### 배운 점

요구사항에 따라서 코드를 작성하는 법을 연습할 수 있었고, python에서의 set() 자료구조 활용법을 익힐 수 있었습니다. 어려운 문제는 아니었지만 set 함수의 여러 메서드들을 써보면서 익힌 덕분에 집합 연산이 필요할 때 잘 활용해볼 수 있을 것 같습니다.

### 문제 설명

비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

### 입력

첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

### 출력

check 연산이 주어질때마다, 결과를 출력한다.

### 예제 입력1

```
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
```

### 예제 출력 1

```
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
```
