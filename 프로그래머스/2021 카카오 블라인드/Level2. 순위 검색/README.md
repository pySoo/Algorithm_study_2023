## [Level 2] 순위 검색 - 72412

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/72412)

### 구분

코딩테스트 연습 > 카카오 2021 블라인드 1차

### 풀이 요약

4가지 조건과 점수가 담긴 질의문을 만족하는 지원자 수를 구하는 구현 및 이분 탐색 문제였습니다.

풀이에서 중요한 점은 효율성을 통과하기 위해서 **해시맵을 만들고 이분 탐색으로 탐색 시간을 줄이는 것**입니다. 이전에는 카카오의 풀이를 참고하여 key 조합을 만드는 방식으로 풀이하였는데, 다시 풀어보니 조합 아이디어를 떠올리고 조합에 대한 문자열을 처리하는 것이 쉽지 않았습니다.

그래서 핵심 아이디어인 **해시맵과 이분 탐색 개념**은 가져가되, **스스로 생각해낸 풀이를 적용**하는 방식으로 다시 풀어봤습니다.

1. 점수를 제외한 참가자 정보를 dictionary의 key로 만듭니다. 단, 문자 사이는 ','가 들어갑니다.
   - 예: { "java,backend,junior,pizza" : [] }
2. dictionary의 value 값은 참가자의 점수를 나타내는 배열로 설정합니다.
   - 예: { "java,backend,junior,pizza" : [200, 150] }
3. 이분 탐색을 위해 dictionary의 점수 값을 정렬합니다.
   - 예: { "java,backend,junior,pizza" : [150, 200] }
4. query 반복문에서 'and'를 기준으로 문자열을 split한 배열을 만들고, '-' 문자는 삭제합니다.
   - 예: cpp and - and senior and pizza 250 -> ["cpp","senior","pizza"]
5. 참가자 정보가 담긴 dictionary 반복문을 돌면서 해당 key가 4번의 query 리스트를 모두 포함했는지 체크합니다. (check_keys)
   - 예: "cpp,backend,senior,pizza" -> ','를 기준으로 문자열 리스트로 만들고, 해당 리스트가 4번의 query 리스트를 모두 포함하는지 체크
   - ["cpp","backend","senior","pizza"]가 ["cpp","senior","pizza"]을 모두 포함하는지 체크
6. 만약 5번을 만족한다면 이분 탐색을 이용하여 원하는 점수 이상의 값이 처음 나오는 위치를 구합니다. (이를 **Lower Bound**라고 부릅니다.)

> 이분 탐색이 '원하는 값을 찾는 과정' 이라면 Lower Bound는 '원하는 값 이상이 처음 나오는 위치를 찾는 과정' 입니다.

### 나의 풀이

```python
from collections import defaultdict

def check_keys(key, query_list):
    key_list = key.split(',')

    cnt = 0
    for key in key_list:
        if key in query_list:
            cnt += 1

    return len(query_list) == cnt


def check_score(values, score):
    start, end = 0, len(values) - 1

    if values[-1] < score:
        return 0

    while start < end:
        mid = (start + end) // 2
        if values[mid] >= score:
            end = mid
        else:
            start = mid + 1

    return len(values) - end



def solution(info, query):
    answer = []
    applicants = defaultdict(list)

    for command in info:
        command = command.split()
        score = int(command[-1])
        parsed_command = ','.join(command[:-1])
        applicants[parsed_command].append(score)

    for key in applicants:
        applicants[key].sort()

    for command in query:
        command_list = command.replace('and','').split()
        score = int(command_list[-1])

        command_list = [x for x in command_list if x != '-'][:-1]

        applicant = 0
        for key, values in applicants.items():
            if check_keys(key, command_list):
                applicant += check_score(values, score)

        answer.append(applicant)

    return answer
```

### 배운 점

위 문제에서는 이분 탐색과 해시맵 활용 방법을 배울 수 있었습니다. 어려웠던 점은 정확히 어떠한 값을 찾는게 아니고, 주어진 값 **이상의 값이 처음 나오는 위치**를 찾는 문제여서 이분 탐색 코드를 수정하는 것이었습니다.

기존의 이분 탐색에서는 정확한 값을 찾기 위해서 값이 일치하지 않을 때 범위를 좁혀주는 식으로 코드를 작성했습니다.

```Python
if values[mid] > score:
    end = mid - 1
elif values[mid] < score:
    start = mid + 1
elif values[mid] == score:
    return mid
```

하지만, 위 문제에서는 주어진 값 이상의 값이 나오는 위치가 필요하므로, 마지막 일치할 때의 케이스를 초과할 때의 케이스와 합치는 것이 필요했습니다.

```Python
if values[mid] >= score:
    end = mid
elif values[mid] < score:
    start = mid + 1
```

이번 문제 풀이를 통해 이러한 탐색 과정을 Lower Bound라고 불리는 것을 알게 되었고 앞으로는 이분 탐색을 더 다양하게 활용해볼 수 있을 것 같습니다.

구현 문제에서 dictionary를 활용하는 문자열 문제는 자주 나오기 때문에 한 번 풀었던 문제라도 다시 풀어보는 연습을 해봐야겠습니다.

### 문제 설명

[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info, 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

<h4>제한사항</h4>

- info 배열의 크기는 1 이상 50,000 이하입니다.
- info 배열 각 원소의 값은 지원자가 지원서에 입력한 4가지 값과 코딩테스트 점수를 합친 "개발언어 직군 경력 소울푸드 점수" 형식입니다.
  - 개발언어는 cpp, java, python 중 하나입니다.
  - 직군은 backend, frontend 중 하나입니다.
  - 경력은 junior, senior 중 하나입니다.
  - 소울푸드는 chicken, pizza 중 하나입니다.
  - 점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수입니다.
  - 각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.
- query 배열의 크기는 1 이상 100,000 이하입니다.
- query의 각 문자열은 "[조건] X" 형식입니다.
  - [조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형식의 문자열입니다.
  - 언어는 cpp, java, python, - 중 하나입니다.
  - 직군은 backend, frontend, - 중 하나입니다.
  - 경력은 junior, senior, - 중 하나입니다.
  - 소울푸드는 chicken, pizza, - 중 하나입니다.
  - '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
  - X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 X점 이상 받은 사람은 모두 몇 명인 지를 의미합니다.
  - 각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.
  - 예를 들면, "cpp and - and senior and pizza 500"은 "cpp로 코딩테스트를 봤으며, 경력은 senior 이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 500점 이상 받은 사람은 모두 몇 명인가?"를 의미합니다.

<h4>입출력 예</h4>
<table>
        <thead><tr>
<th>info</th>
<th>query</th>
<th>result</th>
</tr>
</thead>
        <tbody>
<tr>
<td>["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]</td>
<td>["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]</td>
<td>[1,1,1,1,2,4]</td>
</tr>
</tbody>
      </table>
