## 과제 진행하기 - 176962

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/176962)

### 구분

구현

### 풀이 요약

문제에서 주어진 우선 순위를 고려해서 stack에 있는 과제들을 처리하는 구현 문제였습니다.

문자열 시간을 int로 변환한뒤 남은 시간을 비교해서 stack 요소들을 처리해주면 풀이할 수 있습니다.

### 나의 풀이

```python
def convert_time_to_number(prev, start):
    prev = list(map(int, prev.split(':')))
    start = list(map(int, start.split(':')))
    return (start[0] - prev[0]) * 60 + start[1] - prev[1]

def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])
    doing = [plans.pop(0)]

    for plan in plans:
        name, start, playtime = plan
        if doing:
            prev_name, prev_start, prev_playtime = doing[-1]
            prev_playtime = int(prev_playtime)
            passed_time = convert_time_to_number(prev_start, start)

            if passed_time == prev_playtime:
                doing.pop()
                answer.append(prev_name)
            elif passed_time > prev_playtime:
                while doing:
                    prev_name, prev_start, prev_playtime = doing[-1]
                    prev_playtime = int(prev_playtime)

                    if passed_time >= prev_playtime:
                        doing.pop()
                        answer.append(prev_name)
                        passed_time -= prev_playtime
                    else:
                        doing[-1] = [prev_name, prev_start, prev_playtime - passed_time]
                        break
            elif passed_time < prev_playtime:
                doing[-1] = [prev_name, prev_start, prev_playtime - passed_time]

        doing.append(plan)

    while doing:
        answer.append(doing.pop()[0])

    return answer
```

### 배운 점

stack 자료형을 활용해서 시간 순서대로 요소를 처리하는 방법을 익힐 수 있었습니다. 이전에 카카오 기출에도 시간 순서대로 stack을 이용해서 우선순위를 계산하는 문제가 있었습니다. stack을 사용할 때는 인덱스 에러 처리가 안 나도록 예외처리를 잘 해주어야 한다는 것을 다시금 깨달을 수 있었습니다.

### 문제 설명

과제를 받은 루는 다음과 같은 순서대로 과제를 하려고 계획을 세웠습니다.

과제는 시작하기로 한 시각이 되면 시작합니다.
새로운 과제를 시작할 시각이 되었을 때, 기존에 진행 중이던 과제가 있다면 진행 중이던 과제를 멈추고 새로운 과제를 시작합니다.
진행중이던 과제를 끝냈을 때, 잠시 멈춘 과제가 있다면, 멈춰둔 과제를 이어서 진행합니다.
만약, 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야 하는 과제부터 진행합니다.
멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작합니다.
과제 계획을 담은 이차원 문자열 배열 plans가 매개변수로 주어질 때, 과제를 끝낸 순서대로 이름을 배열에 담아 return 하는 solution 함수를 완성해주세요.

### 제한사항

- 3 ≤ plans의 길이 ≤ 1,000
  - plans의 원소는 [name, start, playtime]의 구조로 이루어져 있습니다.
    - name : 과제의 이름을 의미합니다.
      - 2 ≤ name의 길이 ≤ 10
      - name은 알파벳 소문자로만 이루어져 있습니다.
      - name이 중복되는 원소는 없습니다.
    - start : 과제의 시작 시각을 나타냅니다.
      - "hh:mm"의 형태로 "00:00" ~ "23:59" 사이의 시간값만 들어가 있습니다.
      - 모든 과제의 시작 시각은 달라서 겹칠 일이 없습니다.
      - 과제는 "00:00" ... "23:59" 순으로 시작하면 됩니다. 즉, 시와 분의 값이 작을수록 더 빨리 시작한 과제입니다.
    - playtime : 과제를 마치는데 걸리는 시간을 의미하며, 단위는 분입니다.
      - 1 ≤ playtime ≤ 100
      - playtime은 0으로 시작하지 않습니다.
    - 배열은 시간순으로 정렬되어 있지 않을 수 있습니다.
- 진행중이던 과제가 끝나는 시각과 새로운 과제를 시작해야하는 시각이 같은 경우 진행중이던 과제는 끝난 것으로 판단합니다.
