## [Level 2] 캐시 - 17680

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/17680)

### 구분

코딩테스트 연습 > 카카오 2018 블라인드 1차

### 풀이 요약

주어진 요건대로 LRU 알고리즘을 구현하는 문제.
입력 형식에서 cacheSize가 0인 예외 케이스를 처리하는 것이 중요하다.

### 나의 풀이

```python
from collections import deque

def solution(cache_size, cities):
    answer = 0
    cache_list = deque()

    if cache_size == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache_list:
            answer += 1
            cache_list.remove(city)
        else:
            answer += 5
            if len(cache_list) == cache_size:
                cache_list.popleft()
        cache_list.append(city)

    return answer
```

### 배운 점

입력 형식의 제한 사항을 꼼꼼히 보고 예외 케이스를 생각하는 능력을 기르는게 필요하다는 생각이 들었다. 한 가지 더 배웠던 점은 python의 deque를 활용하는 법이었다. LRU 알고리즘은 선입선출의 방식을 따르는데, deque를 이용하면 양끝의 데이터를 제거하거나 추가하는 처리가 매우 빠르기 때문에 선입선출을 구현하기에 적합했다.

- deque의 popleft(): O(1)
  이유: front와 rear의 값을 가지고 있는 원형 큐의 구조여서 front+=1로 맨 앞의 요소를 삭제하는 것이 가능하다.

- list의 pop(0): O(n)
  이유: 맨 앞의 요소를 삭제 했을 때 배열의 모든 값을 조회하여 앞으로 한 칸 당겨주는게 필요하다.

### 문제 설명

지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

<h4>입력 형식</h4>
캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.

<h4>출력 형식</h4>
입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.

<h4>조건</h4>
캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
cache hit일 경우 실행시간은 1이다.
cache miss일 경우 실행시간은 5이다.

<h4>입출력 예제</h4>
<table>
        <thead><tr>
<th>캐시크기(cacheSize)</th>
<th>도시 이름(cities)</th>
<th>실행시간</th>
</tr>
</thead>
        <tbody>
<tr>
<td>3</td>
<td>["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"</td>
<td>50</td>
</tr>
</tbody>
      </table>
