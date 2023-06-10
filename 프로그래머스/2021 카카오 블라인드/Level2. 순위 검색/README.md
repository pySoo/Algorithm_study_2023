## [Level 2] 순위 검색 - 72412

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/72412)

### 구분

코딩테스트 연습 > 카카오 2021 블라인드 1차

### 풀이 요약

4가지 조건과 점수가 담긴 질의문을 만족하는 지원자 수를 구하는 구현 및 이분 탐색 문제였습니다.

풀이에서 중요한 점은 효율성을 통과하기 위해서 해시맵을 만드는 것입니다. 4가지 조건에 대한 2^4개의 경우를 key로 설정하고, 점수를 value로 설정한 dictionary를 만듭니다. 그리고 점수를 오름차순 정렬하여 이분 탐색을 하여야 문제를 통과할 수 있습니다.

### 나의 풀이

```python
from itertools import combinations
from collections import defaultdict


def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        # 점수 앞에 있는 문자열
        key = info[:-1]
        # 점수
        val = int(info[-1])
        for i in range(5):
            # 하나의 info에서 경우의 수 16개 만들기 -> 항목이 4개이므로
            for combi in combinations(key, i):
                combi_key = ''.join(combi)
                info_dict[combi_key].append(val)

    for key in info_dict.keys():
        # lower bound 사용하기 위해 점수를 오름차순으로 정렬
        info_dict[key].sort()

    for query in queries:
        query = query.split()
        q_score = int(query[-1])
        query = query[:-1]

        # and와 -를 제거하고 하나의 문자열로 만듦 = backendjuniorpizza
        for i in range(3):
            query.remove('and')

        while '-' in query:
            query.remove('-')

        # 리스트를 문자열로
        q_key = ''.join(query)
        if q_key in info_dict:
            scores = info_dict[q_key]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - end)
        else:
            answer.append(0)
    return answer
```

### 배운 점

위 문제에서는 이분 탐색 활용 방법과 문자열로 조합을 만들어서 dictionary의 key로 설정하는 해시맵 활용 방법을 배울 수 있었습니다.

처음 풀이에서는 사용 언어를 key 값으로 설정하여 다시 그 안에서 문자열을 비교하여 찾도록 하였는데 정확성은 통과하였지만 효율성은 통과하지 못했습니다. 카카오 문제 해설을 참고한 바 binary 탐색으로 해결하는 것이 핵심이었습니다.

효율성 정답률은 5퍼센트에 준할 정도로 아이디어를 떠올리는게 매우 어려운 문제였습니다. 그래도 이번 문제를 통해 아이디어를 적용하는 방법을 배워두었으니, 앞으로 정렬과 탐색이 필요한 문제에서는 해당 풀이를 떠올려볼 수 있을 것 같습니다.

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
