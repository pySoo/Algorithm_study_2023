## [Level 1] 성격 유형 검사하기 - 118666

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/118666)

### 구분

코딩테스트 연습 > 2022 카카오 테크 인턴십

### 풀이 요약

요구사항대로 구현하는 구현 문제였습니다. 해시와 배열을 이용해서 검사 점수를 저장하고, 높은 점수의 유형을 출력하여 풀이했습니다.

### 나의 풀이

```python
from collections import defaultdict

def solution(survey, choices):
    answer = ''
    character_type = [('R','T'), ('C','F'), ('J','M'), ('A','N')]
    character_score = defaultdict(int)

    for survey_type, choice in zip(survey, choices):
        type_a, type_b = survey_type[0], survey_type[1]
        if choice < 4:
            character_score[type_a] += 4 - choice
        elif choice > 4:
            character_score[type_b] += choice - 4

    for type_a, type_b in character_type:
        if character_score[type_a] >= character_score[type_b]:
            answer += type_a
        else:
            answer += type_b
    return answer
```

### 배운 점

collections의 defaultdict를 이용하면 저장한 적 없는 key가 들어오더라도 초기값을 0으로 세팅해주어서 오류가 발생하지 않아 편리하다는 것을 알게 되었습니다.

1대1 대응이 되는 관계는 zip으로 묶어서 풀이하는 것이 매우 편리하고 코드 양을 줄여준다는 것을 느끼고 있습니다. 조금이라도 더 알아보기 쉬운 코드를 작성하려고 노력하고 있는데 이렇게 고민하는 과정이 요즘 매우 재밌다고 느낍니다..ㅎㅎ

### 문제 설명

나만의 카카오 성격 유형 검사지를 만들려고 합니다.
성격 유형 검사는 다음과 같은 4개 지표로 성격 유형을 구분합니다. 성격은 각 지표에서 두 유형 중 하나로 결정됩니다.

지표 번호 성격 유형
1번 지표 라이언형(R), 튜브형(T)
2번 지표 콘형(C), 프로도형(F)
3번 지표 제이지형(J), 무지형(M)
4번 지표 어피치형(A), 네오형(N)

4개의 지표가 있으므로 성격 유형은 총 16(=2 x 2 x 2 x 2)가지가 나올 수 있습니다. 예를 들어, "RFMN"이나 "TCMA"와 같은 성격 유형이 있습니다.

검사지에는 총 n개의 질문이 있고, 각 질문에는 아래와 같은 7개의 선택지가 있습니다.

질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey와 검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices가 매개변수로 주어집니다. 이때, 검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return 하도록 solution 함수를 완성해주세요.

<h4>제한사항</h4>

- 1 ≤ survey의 길이 ( = n) ≤ 1,000
  - survey의 원소는 "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나입니다.
  - survey[i]의 첫 번째 캐릭터는 i+1번 질문의 비동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
  - survey[i]의 두 번째 캐릭터는 i+1번 질문의 동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
- choices의 길이 = survey의 길이
  - choices[i]는 검사자가 선택한 i+1번째 질문의 선택지를 의미합니다.
  - 1 ≤ choices의 원소 ≤ 7

<h4>입출력 예</h4>
<table>
        <thead><tr>
<th>survey</th>
<th>choices</th>
<th>result</th>
</tr>
</thead>
        <tbody>
<tr>
<td>["AN", "CF", "MJ", "RT", "NA"]</td>
<td>[5, 3, 2, 7, 5]</td>
<td>"TCMA"</td>
</tr>
</tbody>
      </table>
