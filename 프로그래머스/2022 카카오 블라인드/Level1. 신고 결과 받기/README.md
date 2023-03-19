## [Level 1] 신고 결과 받기 - 92334

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/92334)

### 구분

코딩테스트 연습 > 카카오 2022 블라인드

### 풀이 요약

해시 자료구조를 활용할 수 있는지 묻는 문제. {"신고 당한 유저": [신고한 유저 리스트]}의 구조로 목록을 만들면 된다. 중복 신고를 카운트하면 안되기 때문에 report 리스트를 집합으로 처리하면 편한 문제였다.

### 나의 풀이

```python
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    ban_dict = {id: [] for id in id_list}

    report = set(report)

    for r in report:
        reporter, banned = r.split()
        ban_dict[banned].append(reporter)

    for banned, reporters in ban_dict.items():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[id_list.index(reporter)] += 1

    return answer
```

### 배운 점

중복 신고 처리를 ban_dict[banned]에서 이미 있는 이름이면 추가하지 않는 것으로 처리했는데, set 함수를 이용하면 처음부터 중복을 없앨 수 있어 편리했다. 중복 처리 문제에서는 set을 활용해보자는 아이디어를 얻게 되었다.

그리고 첫 풀이에서는 정답을 출력하기 위해 mail_dict라는 딕셔너리를 만들어서 순회를 한 번 더 했는데 비효율적이라는 생각이 들었다. 다른 분들의 풀이를 참고하였더니 id_list 길이만큼 배열을 할당하고 index()함수를 사용하면 추가 딕셔너리 필요없이 위치를 찾아서 바로 할당할 수 있다는 것을 배울 수 있었다.

### 문제 설명

신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

<h4>제한사항</h4>
- 2 ≤ id_list의 길이 ≤ 1,000
1 ≤ id_list의 원소 길이 ≤ 10
id_list의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
id_list에는 같은 아이디가 중복해서 들어있지 않습니다.

- 1 ≤ report의 길이 ≤ 200,000
  3 ≤ report의 원소 길이 ≤ 21
  report의 원소는 "이용자id 신고한id"형태의 문자열입니다.
  예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.
  id는 알파벳 소문자로만 이루어져 있습니다.
  이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.
  자기 자신을 신고하는 경우는 없습니다.

- 1 ≤ k ≤ 200, k는 자연수입니다.

- return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.

<h4>입출력 예</h4>
<table>
        <thead><tr>
<th>id_list</th>
<th>report</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody>
<tr>
<td>["muzi", "frodo", "apeach", "neo"]</td>
<td>["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]</td>
<td>2</td>
<td>[2,1,1,0]</td>
</tr>
</tbody>
      </table>
