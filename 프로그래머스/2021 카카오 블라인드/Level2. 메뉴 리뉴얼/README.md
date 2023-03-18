## [Level 2] 메뉴 리뉴얼 - 72411

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/72411)

### 구분

코딩테스트 연습 > 카카오 2021 블라인드 1차

### 풀이 요약

조합을 이용하는 구현 문제. 주의할 점은 “ABC”와 “CBA”의 경우 다르게 카운트 되기 때문에, 정렬을 이용해서 하나의 요소로 만들어 주는 것이 필요하다.

### 나의 풀이

```python
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for course_num in course:
        arr = []
        for order in orders:
            combi = combinations(sorted(order), course_num)
            arr.extend(list(combi))

        counter = Counter(arr)

        if len(counter) != 0 and max(counter.values()) != 1:
            max_value = max(counter.values())
            for key in counter:
                if counter[key] == max_value:
                    answer.append(''.join(key))

    return sorted(answer)
```

### 배운 점

Counter를 이용하면 리스트에서 특정 원소가 몇 번 나왔는지 쉽게 계산할 수 있다는 것을 알게 되었다. 위 문제에서는 조건이 해당 조합에서 가장 많이 주문한 요소를 뽑아야 하기 때문에 max value 값을 구하는 것도 필요했는데, counter에는 values()라는 함수로 값만 추출할 수 있었기 때문에 Counter가 문제 구현에 있어서 적합한 모듈이었다. 또한, 조합 문제에서 조합을 카운트 해야할 때 'ABC' 'CBA'와 같이 순서만 다른 경우가 있을 수 있음을 체크해야 한다는 것도 배울 수 있었다.

### 문제 설명

레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고 고민하고 있습니다.
기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다. 어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던 "스카피"는 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.

예를 들어, 손님 6명이 주문한 단품메뉴들의 조합이 다음과 같다면,
(각 손님은 단품메뉴를 2개 이상 주문해야 하며, 각 단품메뉴는 A ~ Z의 알파벳 대문자로 표기합니다.)

각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, "스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, "스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

<h4>제한사항</h4>
- orders 배열의 크기는 2 이상 20 이하입니다.

- orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
  각 문자열은 알파벳 대문자로만 이루어져 있습니다.
  각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.

- course 배열의 크기는 1 이상 10 이하입니다.
  course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
  course 배열에는 같은 값이 중복해서 들어있지 않습니다.

- 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
  배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
  만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
  orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.

<h4>입출력 예</h4>
<table>
        <thead><tr>
<th>orders</th>
<th>course</th>
<th>result</th>
</tr>
</thead>
        <tbody>
<tr>
<td>["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]</td>
<td>[2,3,4]</td>
<td>[2,3,4]</td>
</tr>
</tbody>
      </table>
