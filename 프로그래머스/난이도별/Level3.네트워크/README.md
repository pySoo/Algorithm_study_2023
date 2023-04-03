# [Level 3] 네트워크 - 43162

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)

### 구분

코딩테스트 고득점 Kit > DFS/BFS

### 풀이 요약

DFS 또는 BFS를 이용하여 이어져 있는 노드들을 하나의 군집으로 묶은 뒤 묶여있는 총 군집 수를 구하는 문제

### 나의 풀이

```python
# DFS 풀이
def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]

    def DFS(x):
        visited[x] = True
        for i in range(n):
            if x != i and computers[x][i] == computers[i][x] == 1:
                if not visited[i]:
                    DFS(i)


    for com in range(n):
        if not visited[com]:
            DFS(com)
            answer += 1

    return answer

# BFS 풀이
from collections import deque

def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]

    def BFS(com):
        queue = deque()
        queue.append(com)
        while queue:
            x = queue.popleft()
            visited[x] = True
            for i in range(n):
                if x != i and computers[x][i] == computers[i][x] == 1:
                    if not visited[i]:
                        queue.append(i)


    for com in range(n):
        if not visited[com]:
            BFS(com)
            answer += 1

    return answer
```

### 배운 점

앞서 BFS를 이용해 풀었던 ["게임 맵 최단거리"](https://velog.io/@soopy368/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Python-%EA%B2%8C%EC%9E%84-%EB%A7%B5-%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC-BFS) 문제에서는 무조건 같은 위치에서 시작하고 끝 노드까지 걸리는 최단거리를 구하는 것이고 이번 문제에서는 묶여있는 군집의 수를 구해야 했다. 따라서 구현 방법이 조금 다르다.

첫 노드를 넣고 BFS를 돌리는 것이 아니라, 첫 노드가 고립된 경우일 수도 있으므로 모든 노드에 대해서 방문하지 않은 경우 BFS를 돌려야 하고 끝난 경우 군집 수를 1씩 늘려주는 방식으로 구했다.

역시 같은 그래프 탐색 문제여도 요구사항에 따라 유연하게 코드를 수정할 줄 아는 능력이 중요한 것 같다. 이번 문제에서도 익숙한 구현 방식으로만 짜려고 하다보니 처음엔 틀린 구현을 하게 되었다. 다양한 그래프 문제를 풀어보면서 감을 익히도록 해야겠다.

[DFS/BFS 개념 정리](https://velog.io/@soopy368/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%9E%98%ED%94%84-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-DFSBFS-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC)

### 문제 설명

네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

<h5>제한사항</h5>

- 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
- 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
- i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
- computer[i][i]는 항상 1입니다.

<h5>입출력 예</h5>
<table>
<thead><tr>
<th>n</th>
<th>computers</th>
<th>return</th>
</tr>
</thead>
<tbody><tr>
<td>3</td>
<td>[[1, 1, 0], [1, 1, 0], [0, 0, 1]]</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td>[[1, 1, 0], [1, 1, 1], [0, 1, 1]]</td>
<td>1</td>
</tr>
</tbody>
</table>
