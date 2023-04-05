## [Level 3] 여행경로 - 43164

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43164)

### 구분

코딩테스트 고득점 Kit > DFS/BFS

### 풀이 요약

DFS를 이용하여 모든 지점을 순회하는 경로를 찾는 문제. 단, 알파벳 순서가 앞서는 경로로 만들어야 한다.

### 나의 풀이

```python
from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    for (start, end) in tickets:
        graph[start].append(end)

    for airport in graph:
        graph[airport].sort(reverse=True)

    path = []
    stack = ["ICN"]
    while stack:
        route = stack[-1]
        if not graph[route]:
            path.append(stack.pop())
        else:
            next_route = graph[route].pop()
            stack.append(next_route)

    return path[::-1]
```

### 배운 점

이번 문제는 모든 지점을 순회하는 완전 탐색이 필요했기 때문에 DFS를 선택해서 문제를 풀었다. 풀이 아이디어를 떠올리는 것은 어렵지 않았으나 예외 케이스를 생각 못해서 계속 특정 문제에서 틀리곤 했다.

**모든 정점을 방문하는 것이 요구사항**인데 BFS로 풀이하는 경우 첫 경로에서 갈 곳이 없는 경우의 예외 케이스를 처리하기 어렵기 때문에 **모든 지점을 순회하는 DFS가 풀이에 적합했다.**

예외 case:

1. "ICN" -> "BOO"
2. "ICN" -> "COO"
3. "COO" -> "ICN"

알파벳 순서가 앞서는 경로를 만들어 주어야 하기 때문에 처음엔 1번 경로를 선택해야 한다. 하지만, "BOO"로 시작하는 경로가 없기 때문에 BFS를 이용했다면 이전으로 돌아가서 다시 탐색하지 못한다. 그렇기 때문에 DFS를 이용해서 2번을 다시 선택한다. 그 후로는 순서대로 3번, 1번을 선택하여 "ICN->COO->ICN->BOO"의 루트를 완성한다.

BFS 풀이가 조금 더 손에 익어서 이번 문제도 BFS로 풀면 되겠지 하고 쉽게 생각하다가 큰코 다쳤다.. 다음부터는 문제를 풀 때 왜 이러한 알고리즘이 이 문제에 필요한지 논리적으로 생각하는 시간을 충분히 가지고 구현을 해야겠다. 어떤 알고리즘을 택할 지 모를 때는 알고리즘의 특징에 대해 다시 공부하고 이 문제에서 적용했을 때 어떠한 점이 적합하고 장점인지 생각해보는 습관을 들이도록 해보자!

### 문제 설명

주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

<h5>제한사항</h5>

- 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
- 주어진 공항 수는 3개 이상 10,000개 이하입니다.
- tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
- 주어진 항공권은 모두 사용해야 합니다.
- 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
- 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

<h5>입출력 예</h5>
<table>
<thead><tr>
<th>tickets</th>
<th>return</th>
</tr>
</thead>
<tbody><tr>
<td>[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]</td>
<td>["ICN", "JFK", "HND", "IAD"]</td>
</tr>
<tr>
<td>[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]</td>
<td>["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]</td>
</tr>
</tbody>
</table>
