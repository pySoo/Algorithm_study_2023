## [Level 1] 부족한 금액 계산하기 - 82612

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/82612)

### 풀이 요약

네이버 2021 상반기 기출 문제. 문제의 요건대로 구현하면 되는 문제였다.

### 나의 풀이
```python
def solution(price, money, count):
    pay = sum([price * i  for i in range(1, count+1)])
    
    if money > pay:
        return 0
    else:
        return pay - money
```

### 배운 점

주어진대로 구현하면 되는 간단한 문제였지만 조금 더 pythonic하게 코드를 짜고 싶었다. 처음에는 for문을 돌려서 pay에 값을 더해가는 코드로 짰었는데, list 안에 for문을 넣고 sum 함수를 이용하면 한 줄의 코드로 가격의 총합을 구할 수 있다는 것을 알게 되었다.

### 구분

코딩테스트 연습 > 위클리 챌린지 > 구현

### 문제 설명

새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
단, 금액이 부족하지 않으면 0을 return 하세요.

<h5>제한사항</h5>
놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>price</th>
<th>money</th>
<th>count</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>20</td>
<td>4</td>
<td>10</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>
입출력 예 #1
이용금액이 3인 놀이기구를 4번 타고 싶은 고객이 현재 가진 금액이 20이라면, 총 필요한 놀이기구의 이용 금액은 30 (= 3+6+9+12) 이 되어 10만큼 부족하므로 10을 return 합니다.
