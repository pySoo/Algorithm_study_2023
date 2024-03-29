## 동전 0 - 11047

[문제 링크](https://www.acmicpc.net/problem/11047)

### 구분

그리디

### 풀이 요약

가장 큰 동전부터 시작해서 몫을 카운트 해주고, 나머지 동전을 내림차순으로 반복하는 그리디 문제였습니다. 그리디의 대표 유형 문제입니다.

### 나의 풀이

```python
import sys

input = sys.stdin.readline

n, k = map(int,input().split())
coins = []
answer = 0

for _ in range(n):
  coins.append(int(input()))

for i in range(n-1, -1, -1):
  q, r = divmod(k, coins[i])
  answer += q
  k = r

print(answer)
```

### 배운 점

그리디 문제를 쭉 풀어보면서 그리디 아이디어를 떠올리는 것에 대해 조금은 익숙해진 것 같습니다. 위 문제는 DP를 이용해서 풀 수도 있지 않을까라는 생각이 들었는데, k의 값이 1억까지 주어지기 때문에 메모리 초과로 인해 불가능하다는 것을 알게 되었습니다. DP의 경우 1부터 k까지의 모든 경우의 수를 계산하기 때문에 시공간 복잡도를 잘 고려해야겠습니다.

**DP와 그리디의 공통점과 차이점**에 대해서 정리해보고자 합니다!

### 공통점

- 최적 부분 구조 문제를 풀이하는데 사용되는 알고리즘

### DP

- 문제를 작은 단위로 분할하여 해결한 후, 해결된 중복 문제들의 결과를 기반으로 전체 문제를 해결합니다.
- 모든 경우를 조사하기 때문에 최적해의 해답으로서의 신뢰도가 높습니다.
- 하지만 모든 경우의 결과를 저장해두기 때문에 시공간복잡도가 높습니다.

### 그리디

- 각 단계마다 최적해를 찾는 문제로 접근합니다.
- 해결해야 할 전체 문제의 개수를 줄이기 위해 개별적으로 문제를 해결해나가는 선택을 합니다.
- 매 순간 최적의 선택을 하는 ‘근사 알고리즘’으로, 구한 최적해가 일반해일 수도 있고 일반해에 가까운 근사값 일수도 있습니다.
- 시공간복잡도가 낮아서 빠른 계산이 가능합니다.

### 문제 설명

준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

### 입력

첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

### 출력

첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

### 예제 입력 1

```
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
```

### 예제 출력 1

```
6
```
