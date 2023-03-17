## [Level 2] 문자열 압축 - 60057

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/60057)

### 구분

코딩테스트 연습 > 카카오 2020 블라인드 1차

### 풀이 요약

문자열 처리와 완전 탐색 문제. 아래의 작업을 수행하면 된다.

- 문자열 자르기
- 부분 문자열 얻기
- 문자열 비교하기
- 문자열 길이 얻기

### 나의 풀이

```python
def solution(s):
    answer = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2 + 1):
        result = ''
        tmp = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt) + tmp
                else:
                    result += tmp
                cnt = 1
                tmp = s[j:j+i]
        if cnt > 1:
            result += str(cnt) + tmp
        else:
            result += tmp
        answer.append(len(result))
    return min(answer)
```

### 배운 점

n의 크기가 크지 않을 때는 완전 탐색이 가능한지 가장 먼저 고려하고 풀이하는게 빠른 풀이에 도움이 되는 것 같다. 문자열을 특정 구간만큼 건너뛰어 접근해야 할 때는 for 문의 3번째 파라미터를 이용하면 된다는 것을 알게 되었다.

### 문제 설명

데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다. "어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

<h4>제한사항</h4>
- s의 길이는 1 이상 1,000 이하입니다.
- s는 알파벳 소문자로만 이루어져 있습니다.

<h4>입출력 예</h4>
<table>
        <thead><tr>
<th>s</th>
<th>result</th>
</tr>
</thead>
        <tbody>
<tr>
<td>"aabbaccc"</td>
<td>7</td>
</tr>
<tr>
<td>"ababcdcdababcdcd"</td>
<td>9</td>
</tr>
</tbody>
      </table>
