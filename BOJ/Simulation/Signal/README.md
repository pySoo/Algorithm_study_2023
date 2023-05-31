## Signal - 16113

[문제 링크](https://www.acmicpc.net/problem/16506)

### 구분

구현, 문자열

### 풀이 요약

규칙이 있는 문자열을 분석해서 해당 문자열이 나타내는 숫자를 찾아내는 문제였습니다. 이전에 풀었던 LCD Test와 비슷한 문제였지만 구현 방식이 반대였습니다. LCD Test는 숫자를 그리는데 필요한 문자열을 구하는 문제였다면, 이번 문제는 **주어진 문자열을 해독해서 숫자를 찾아내는 것**이었습니다ㅏ. 더 어려운 점이 있었다면 1의 경우만 1열을 차지했기 때문에 중간 과정에서 오류가 발생하였습니다. 코드도 복잡해지고 구현에만 2시간 이상이 걸려서.. (정신이 혼미해졌다 🤯 😭) 결국 다른 사람의 풀이를 참고하여 아이디어를 배울 수 있었습니다!

알고리즘은 다음과 같습니다.

1. 첫 행에서 ‘#’을 발견하면 새로운 숫자가 시작된다.
2. 가장 획이 많은 8에 대한 템플릿 문자열 배열을 만든다.
3. 각 숫자별로 8과 달리 빈 공간의 위치를 선언해두고, 빈 공간이 일치한다면 해당 숫자를 리턴한다.
4. 만약 숫자가 1이라면 1행을 차지하고 공백을 유지해야하므로 2칸을 이동하고, 그렇지 않다면 4칸을 이동한다.

여기서의 핵심은 가장 획이 많은 8에 대한 배열을 만들고 8과 다른 공간을 비교하여 숫자를 찾는 것입니다.

### 나의 풀이

```python
n = int(input())
signal = input()

col_length = 5
row_length = len(signal) // col_length

board = []

for i in range(col_length):
  sliced_row = list(signal[i*row_length:(i+1)*row_length])
  board.append(sliced_row)

template = [[] for _ in range(col_length)]

def get_number(board):
  diff = []
  for col in range(col_length):
    for row in range(3):
      if template[col][row] != board[col][row]:
        diff.append([col,row])
  if [0, 1] in diff and [2, 1] in diff and [4, 1] in diff:
    return 1
  elif diff == [[1,0],[3,2]]:
    return 2
  elif diff == [[1,0],[3,0]]:
    return 3
  elif diff == [[0,1],[3,0],[4,0],[4,1]]:
    return 4
  elif diff == [[1,2],[3,0]]:
    return 5
  elif diff == [[1,2]]:
    return 6
  elif diff == [[1,0],[2,0],[2,1],[3,0],[4,0],[4,1]]:
    return 7
  elif len(diff) == 0:
    return 8
  elif diff == [[3,0]]:
    return 9
  else:
    return 0

for row in range(3):
  for col in range(col_length):
    if col in [1,3] and row in [1]:
      template[col].append('.')
    else:
      template[col].append('#')

answer = ''
row = 0

while row < row_length:
  part = [[] for _ in range(col_length)]
  num = 0
  if board[0][row] == '#':
    for col in range(5):
      part[col].extend(board[col][row:row+3])
      part[col].extend(['.'] * (3-len(part[col])))
    num = get_number(part)
    answer += str(num)
    if num == 1:
      row += 2
    else:
      row += 4
  else:
    row += 1

print(answer)
```

### 배운 점

구현은 주어진 요구사항 대로만 차근차근 퀘스트 깨듯이 풀면 되는 문제도 있지만 어렵게 낸다면 한없이 어려운 것 같습니다. 문자열 처리와 같은 경우 실수를 할 확률이 높아지기 때문에 더 주의해야겠다고 느낍니다.

그래도 LCD Test와 이번 문제를 통해서 보드 형식의 숫자를 문자열로 변환하는 방식에 꽤나 단련되었기 때문에 다음에 동일한 유형을 만난다면 잘 대처할 수 있지 않을까…! 바래봅니다.. (제발~)

### 문제 설명

zxcvber는 외계인을 연구하는 과학자다. 그는 지난 10년간 우주에서 오는 시그널를 연구했지만, 아무런 성과가 없었다. 그러던 어느 날, 갑자기 우주에서 이상한 시그널이 오기 시작했다. zxcvber는 매우 기뻐하며 시그널을 받아서 분석해보았다. 시그널은 0과 1로 이루어져 있는데, 여기서는 편의상 0을 "`.`", 1을 "`#`"으로 표시한다. 시그널은 다음과 같았다.

`###.....###.#..####.#.......#.#....####.....###.#....##.#.......#.#....####.....###.#....#`

https://upload.acmicpc.net/4a8010ac-92da-4b26-8d97-9c9bce4cf931/-/preview/

다른 여러 시그널들을 분석해본 결과, zxcvber는 시그널의 길이가 항상 5의 배수라는 것을 알게 되었다. 시그널을 다섯 개로 쪼개면 뭔가 규칙이 보이지 않을까 생각한 zxcvber는 시그널을 같은 길이의 5개의 시그널로 쪼갰다. 그러자 놀라운 일이 벌어졌다.

시그널은 디지털 숫자를 나타내고 있었다! 1-3열에 8, 9-11열에 3, 13열에 1, 그리고 16-18열에 7이 나타난 것이다. 이 숫자들이 특별한 의미를 갖고 있을 것이라 생각한 zxcvber는 다른 시그널들도 해독을 하기 시작했다. 하지만 시그널들의 길이가 너무 길어서, 일일히 손으로 확인하기에는 한계가 있었다. 다만, 짧은 시그널들을 분석하면서 zxcvber는 시그널의 규칙들을 파악할 수 있었다.

1. 시그널은 "`.`"과 "`#`"으로 이루어져 있다.

2. 시그널을 해독한 결과에는 반드시 숫자가 1개 이상 있다.

3. 시그널에 등장하는 모든 "`#`"은 올바른 숫자 패턴에 포함되어 있다.

4. 숫자와 숫자 사이에는 1열 이상의 공백이 있다. 여기서 공백은, 열의 성분이 모두 "`.`"인 열을 의미한다.

5. 0부터 9는 아래와 같이 나타난다. 역시 "`#`"을 검은색, "`.`"을 흰색으로 표시했다.

https://upload.acmicpc.net/309fd7f3-22b9-452e-95f6-e3f4828c0f9a/-/preview/

주의할 점은, 1은 다른 숫자들과는 다르게 1열을 차지한다는 것이다. zxcvber를 도와 시그널을 해독해보자!

### 입력

입력의 첫 줄에는 시그널의 길이 *N*(5 ≤ *N* ≤ 100,000, *N*은 5의 배수)이 주어진다.

다음 줄에 시그널이 주어진다. zxcvber가 찾아낸 규칙을 따르는 시그널만이 입력으로 주어진다.

### 출력

첫 번째 줄에 시그널을 해독하여 나오는 숫자들을 순서대로 출력한다.

### 예제 입력1

```python
40
###..#..#.#..#..###..#..#.#..#..###..#..
```

### 예제 출력 1

```python
81
```
