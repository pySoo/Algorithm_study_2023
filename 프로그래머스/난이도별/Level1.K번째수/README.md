# [Level 1] K번째수 - 42748

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42748)

### 풀이 요약

배열의 인덱스와 정렬을 활용하는 문제.

### 배운 점

python의 리스트를 활용하는 기본적인 문제였지만, map과 lambda 함수를 이용한 풀이를 보고 두 함수의 사용법을 새로 익힐 수 있었다.

<br />

- map, lambda 이용 풀이

```python
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```

- map(함수, 리스트): 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해 사용
- lambda 매개변수 : 표현식 (이름 없는 함수라고 생각)

```python
# 일반 함수
>>> def hap(x, y):
...   return x + y
...
>>> hap(10, 20)
30

# 람다 형식으로 표현
>>> (lambda x,y: x + y)(10, 20)
30
```

### 구분

코딩테스트 연습 > 정렬

### 문제 설명

<p>배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.</p>

<p>예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면</p>

<ol>
<li>array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.</li>
<li>1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.</li>
<li>2에서 나온 배열의 3번째 숫자는 5입니다.</li>
</ol>

<p>배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>array의 길이는 1 이상 100 이하입니다.</li>
<li>array의 각 원소는 1 이상 100 이하입니다.</li>
<li>commands의 길이는 1 이상 50 이하입니다.</li>
<li>commands의 각 원소는 길이가 3입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>array</th>
<th>commands</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 5, 2, 6, 3, 7, 4]</td>
<td>[[2, 5, 3], [4, 4, 1], [1, 7, 3]]</td>
<td>[5, 6, 3]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.<br>
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.<br>
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.</p>
