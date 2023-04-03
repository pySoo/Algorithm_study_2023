# [Level 2] 게임 맵 최단거리 - 1844

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/1844)

### 구분

코딩테스트 고득점 Kit > DFS/BFS

### 풀이 요약

BFS를 활용해서 최단거리를 구하는 문제

### 나의 풀이

```python
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    queue = deque()
    queue.append((0,0))

    visited = [[False for _ in range(m)] for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        if x == n-1 and y == m-1:
            return maps[n-1][m-1]

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    maps[nx][ny] = maps[x][y] + 1
                    visited[nx][ny] = True
                    queue.append((nx,ny))

    return -1
```

### 배운 점

최단거리를 구하는 문제에서 DFS/BFS 중 무엇을 사용하는 것이 적합한지 익힐 수 있었다. 그래프 탐색 문제를 풀면서 DFS와 BFS의 차이에 대해서 정리해보는 시간을 가졌다. [DFS/BFS 개념 정리](https://velog.io/@soopy368/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%9E%98%ED%94%84-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-DFSBFS-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC)

### 문제 설명

ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.

지금부터 당신은 한 팀의 팀원이 되어 게임을 진행하려고 합니다. 다음은 5 x 5 크기의 맵에, 당신의 캐릭터가 (행: 1, 열: 1) 위치에 있고, 상대 팀 진영은 (행: 5, 열: 5) 위치에 있는 경우의 예시입니다.

위 그림에서 검은색 부분은 벽으로 막혀있어 갈 수 없는 길이며, 흰색 부분은 갈 수 있는 길입니다. 캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 게임 맵을 벗어난 길은 갈 수 없습니다.
아래 예시는 캐릭터가 상대 팀 진영으로 가는 두 가지 방법을 나타내고 있습니다.

- 첫 번째 방법은 11개의 칸을 지나서 상대 팀 진영에 도착했습니다.
- 두 번째 방법은 15개의 칸을 지나서 상대팀 진영에 도착했습니다.

위 예시에서는 첫 번째 방법보다 더 빠르게 상대팀 진영에 도착하는 방법은 없으므로, 이 방법이 상대 팀 진영으로 가는 가장 빠른 방법입니다.

만약, 상대 팀이 자신의 팀 진영 주위에 벽을 세워두었다면 상대 팀 진영에 도착하지 못할 수도 있습니다. 예를 들어, 다음과 같은 경우에 당신의 캐릭터는 상대 팀 진영에 도착할 수 없습니다.

게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

<h5>제한사항</h5>
- maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
    n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
- maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
- 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

<h5>입출력 예</h5>
<table>
<thead><tr>
<th>maps</th>
<th>answer</th>
</tr>
</thead>
<tbody><tr>
<td>[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]</td>
<td>11</td>
</tr>
<tr>
<td>[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]</td>
<td>-1</td>
</tr>
</tbody>
</table>
