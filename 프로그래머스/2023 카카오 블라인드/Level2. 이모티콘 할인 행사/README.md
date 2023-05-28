## [Level 2] 이모티콘 할인 행사 - 150368

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/150368)

### 구분

코딩테스트 연습 > 카카오 2023 블라인드

### 풀이 요약

가능한 모든 경우의 수를 탐색하면 되는 완전 탐색 문제였습니다. 완탐으로 풀이할 때는 시간 초과가 나지 않는지 반드시 확인하는 것이 필요합니다.

이 문제의 경우 할인율이 4가지이고 이모티콘이 m개가 있으므로 이모티콘을 할인하는 경우의 수는 4^m입니다.

각 사용자들이 이모티콘을 구매하는 경우의 수는 n x m이므로, 이모티콘에 할인을 적용하는 경우까지 포함한다면 총 O(4^m x n x m)의 시간복잡도를 가집니다.

4^m의 경우에서 m이 7이기 때문에 최대 경우의 수는 16,384가지 밖에 되지 않습니다. 따라서 제한 시간 안에 모든 경우의 수를 탐색할 수 있습니다!

### 나의 풀이

```python

from itertools import product

def solution(users, emoticons):
    answer = []
    discount_list = [40, 30, 20, 10]
    discount_product = list(product(discount_list, repeat = len(emoticons)))

    for discount_tuple in discount_product:
        total_buy = 0
        total_pay = 0
        for min_discount, max_pay in users:
            user_pay = 0
            for discount, emoticon_pay in zip(discount_tuple, emoticons):
                if discount >= min_discount:
                    user_pay += int(emoticon_pay * (100 - discount) * 0.01)
            if user_pay >= max_pay:
                total_buy += 1
            else:
                total_pay += user_pay
        answer.append([total_buy, total_pay])

    return sorted(answer, key = lambda x: (x[0], x[1]))[-1]

```

### 배운 점

이전에는 input의 값이 작으면 어림짐작으로 시간 초과가 나지 않을 것이라 예상하기도 했었는데, 이번 문제에서는 미리 시간 복잡도를 계산하여 시간 초과가 발생하지 않는지 판단하는 능력을 기를 수 있어서 유익했습니다. 앞으로도 알고리즘을 풀 때 시간 복잡도를 계산하는 습관을 들이도록 해야겠습니다.

그리고 python에서 중복 순열을 뽑는 product 툴에 대해서 알게 되었습니다. 기존 방식대로 permutation을 사용하려 했으나, 이 문제에서는 (40%, 40%)와 같이 중복된 요소를 뽑는 것이 중요했기 때문에 product를 사용하여 풀이하였습니다.

조합, 순열, 중복 순열의 개념이 헷갈릴 수 있기 때문에 정리해보고자 합니다.

arr = ['A', 'B', 'C']

- comination: 순서를 고려하지 않고, 중복 없이 n개 중 r개를 뽑는 것
  - [('A','B'), ('A','C'), ('B','C')]
- permutation: 순서를 고려해서, 중복 없이 n개 중 r개를 뽑는 것
  - [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]
- product: 중복을 포함하여 모든 순열을 구하는 것
  - [('A','A'), ('B','B'), ('C','C'), ... permutation]

### 문제 설명

카카오톡에서는 이모티콘을 무제한으로 사용할 수 있는 이모티콘 플러스 서비스 가입자 수를 늘리려고 합니다.
이를 위해 카카오톡에서는 이모티콘 할인 행사를 하는데, 목표는 다음과 같습니다.

이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
이모티콘 판매액을 최대한 늘리는 것.
1번 목표가 우선이며, 2번 목표가 그 다음입니다.

이모티콘 할인 행사는 다음과 같은 방식으로 진행됩니다.

n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매합니다.
이모티콘마다 할인율은 다를 수 있으며, 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다.
카카오톡 사용자들은 다음과 같은 기준을 따라 이모티콘을 사거나, 이모티콘 플러스 서비스에 가입합니다.

각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매합니다.
각 사용자들은 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입합니다.

카카오톡 사용자 n명의 구매 기준을 담은 2차원 정수 배열 users, 이모티콘 m개의 정가를 담은 1차원 정수 배열 emoticons가 주어집니다. 이때, 행사 목적을 최대한으로 달성했을 때의 이모티콘 플러스 서비스 가입 수와 이모티콘 매출액을 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해주세요.

<h4>제한사항</h4>

- 1 ≤ users의 길이 = n ≤ 100
  - users의 원소는 [비율, 가격]의 형태입니다.
  - users[i]는 i+1번 고객의 구매 기준을 의미합니다.
  - 비율% 이상의 할인이 있는 이모티콘을 모두 구매한다는 의미입니다.
    - 1 ≤ 비율 ≤ 40
  - 가격이상의 돈을 이모티콘 구매에 사용한다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입한다는 의미입니다.
    - 100 ≤ 가격 ≤ 1,000,000
    - 가격은 100의 배수입니다.
- 1 ≤ emoticons의 길이 = m ≤ 7
  - emoticons[i]는 i+1번 이모티콘의 정가를 의미합니다.
  - 100 ≤ emoticons의 원소 ≤ 1,000,000
  - emoticons의 원소는 100의 배수입니다.

<h4>입출력 예</h4>
<table>
        <thead><tr>
<th>users</th>
<th>emoticons</th>
<th>result</th>
</tr>
</thead>
        <tbody>
<tr>
<td>[[40, 10000], [25, 10000]]</td>
<td>[7000, 9000]</td>
<td>[1, 5400]</td>
</tr>
</tbody>
      </table>
