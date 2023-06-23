## [Level 2] 프렌즈 4블록 - 17679

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/17679)

### 구분

코딩테스트 연습 > 카카오 2018 블라인드 1차

### 풀이 요약

주어진 요건대로 인접한 블록 매트릭스를 제거하는 구현 문제입니다. 2x2 모양이 같다면 터트릴 블록 집합에 인덱스를 넣어주고 터트렸다는 것을 알 수 있도록 값을 '-'로 설정합니다. 블록을 터트린 후에는 요소들을 아래로 내려주는 작업이 필요했습니다.

이전에는 행과 열을 바꿔서 풀이했지만 시험 당일과 같이 긴장되는 상황에서는 오히려 실수를 유발할 수 있을 것 같아서 순서대로 블록을 내려주는 방식으로 바꿔서 다시 풀어보았습니다.

### 나의 풀이

````python
def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]

    def pop_board(x,y):
        block = board[x][y]
        pop_set = set()
        if board[x+1][y] == board[x][y+1] == board[x+1][y+1] == block:
            pop_set = {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}
        return pop_set

    def down_board(board):
        for y in range(n):
            for x in range(m-2,-1,-1):
                for next_x in range(m-1, x, -1):
                    if board[x][y] != '-' and board[next_x][y] == '-':
                        board[next_x][y] = board[x][y]
                        board[x][y] = '-'

    while True:
        pop_set = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '-':
                    pop_set.update(pop_board(i,j))

        if pop_set:
            answer += len(pop_set)
            for x,y in pop_set:
                board[x][y] = '-'
            down_board(board)
        else:
            break

    return answer


### 배운 점

백준의 Puyo Puyo라는 문제와 매우 비슷한 문제였습니다. 2x2 모양을 발견할 때마다 터트려주는게 아니라, 모든 모양을 발견한 후 한 번에 터트려주는 것이 필요했기 때문에 pop_set에 터트릴 인덱스를 모았다가 한 번에 터트려주었습니다. 그리고 중복되는 인덱스가 있기 때문에 set 자료형을 사용하였습니다.

이번 풀이에서 또 헷갈렸던 점은 원소들을 y축 아래로 내려주는 작업이었습니다. 첫 풀이에서는 행을 위에서부터 아래로 내려주었는데 (for x in range(m)), 이렇게 되면 내려준 요소를 다음 반복문에서 또 접근할 수 있게 됩니다. 따라서 내릴 요소가 1개라도 있는 m-2행부터 0번째 행까지의 역순으로 (for x in range(m-2, -1, -1)) 요소를 내려주는 것이 필요했습니다.

```python
 def down_board(board):
        for y in range(n):
            for x in range(m-2,-1,-1):
                for next_x in range(m-1, x, -1):
                    if board[x][y] != '-' and board[next_x][y] == '-':
                        board[next_x][y] = board[x][y]
                        board[x][y] = '-'
```

### 문제 설명

블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.

블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.

만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.

위 초기 배치를 문자로 표시하면 아래와 같다.

TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ

각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

<h4>입력 형식</h4>
- 입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
- 2 ≦ n, m ≦ 30
- board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.

<h4>출력 형식</h4>
입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.

<h4>입출력 예제</h4>
<table>
        <thead><tr>
<th>m</th>
<th>n</th>
<th>board</th>
<th>answer</th>
</tr>
</thead>
        <tbody>
<tr>
<td>4</td>
<td>5</td>
<td>["CCBDE", "AAADE", "AAABF", "CCBBF"]</td>
<td>14</td>
</tr>
</tbody>
      </table>
````
