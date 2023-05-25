## [Level 1] 개인정보 수집 유효기간 - 150370

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/150370)

### 구분

코딩테스트 연습 > 카카오 2023 블라인드

### 풀이 요약

해시 테이블을 이용해서 약관별 유효 기간을 저장하고, 각 개인정보와 연결지어서 보관 가능한 날짜를 계산하는 문제이다. 보관 가능한 날짜와 오늘 날짜를 정수 형태로 변환하여 비교하고 유효기간이 지난 개인정보를 출력한다.

### 나의 풀이

```python
def convert_date_to_int(date):
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    for term in terms:
        term_type, month = term.split()
        term_dict[term_type] = int(month) * 28

    for i in range(len(privacies)):
        date, term_type = privacies[i].split()
        due_date = convert_date_to_int(date) + term_dict[term_type]
        if due_date <= convert_date_to_int(today):
            answer.append(i+1)

    return answer
```

### 배운 점

문자열을 적절하게 분리해서 날짜를 계산하는 문제였다. 파이썬에서 문자열 x 숫자를 하면 해당 문자열이 숫자만큼 출력되기 때문에, map을 이용해서 int로 변환해주는 것이 필요했다. 입력 형식을 꼼꼼히 체크해서 변환하는 것이 중요하다는 것을 배웠다.

그리고 날짜를 정수 형태로 변환해주는 함수를 만들어서 관심사의 분리 원칙을 지키려고 노력했다. 앞으로도 코딩 테스트에서 정답 맞추기에만 집중하기보다는 채점자도 쉽게 이해할 수 있도록 코드를 작성하려고 한다.

### 문제 설명

고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다. 당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다. 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.

예를 들어, A라는 약관의 유효기간이 12 달이고, 2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면 해당 개인정보는 2022년 1월 4일까지 보관 가능하며 2022년 1월 5일부터 파기해야 할 개인정보입니다.
당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.

모든 달은 28일까지 있다고 가정합니다.

오늘 날짜를 의미하는 문자열 today, 약관의 유효기간을 담은 1차원 문자열 배열 terms와 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수로 주어집니다. 이때 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

<h4>제한사항</h4>

- today는 "YYYY.MM.DD" 형태로 오늘 날짜를 나타냅니다.
- 1 ≤ terms의 길이 ≤ 20
  - terms의 원소는 "약관 종류 유효기간" 형태의 약관 종류와 유효기간을 공백 하나로 구분한 문자열입니다.
  - 약관 종류는 A~Z중 알파벳 대문자 하나이며, terms 배열에서 약관 종류는 중복되지 않습니다.
  - 유효기간은 개인정보를 보관할 수 있는 달 수를 나타내는 정수이며, 1 이상 100 이하입니다.
- 1 ≤ privacies의 길이 ≤ 100
  - privacies[i]는 i+1번 개인정보의 수집 일자와 약관 종류를 나타냅니다.
  - privacies의 원소는 "날짜 약관 종류" 형태의 날짜와 약관 종류를 공백 하나로 구분한 문자열입니다.
  - 날짜는 "YYYY.MM.DD" 형태의 개인정보가 수집된 날짜를 나타내며, today 이전의 날짜만 주어집니다.
  - privacies의 약관 종류는 항상 terms에 나타난 약관 종류만 주어집니다.
- today와 privacies에 등장하는 날짜의 YYYY는 연도, MM은 월, DD는 일을 나타내며 점(.) 하나로 구분되어 있습니다.
  - 2000 ≤ YYYY ≤ 2022
  - 1 ≤ MM ≤ 12
  - MM이 한 자릿수인 경우 앞에 0이 붙습니다.
  - 1 ≤ DD ≤ 28
  - DD가 한 자릿수인 경우 앞에 0이 붙습니다.
- 파기해야 할 개인정보가 하나 이상 존재하는 입력만 주어집니다.

<h4>입출력 예</h4>
<table>
        <thead><tr>
<th>today</th>
<th>terms</th>
<th>privacies</th>
<th>result</th>
</tr>
</thead>
        <tbody>
<tr>
<td>"2022.05.19"</td>
<td>["A 6", "B 12", "C 3"]</td>
<td>["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]</td>
<td>[1, 3]</td>
</tr>
</tbody>
      </table>
