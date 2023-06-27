## 모음 사전 - 84512

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/84512)

### 구분

완전탐색

### 풀이 요약

DFS를 통해 dictionary에 가능한 모든 경우의 수를 넣어서 풀이했습니다. 현재 문자열의 길이가 5보다 작다면 문자열에 다음 문자를 붙여서 DFS를 실행하는 방식입니다.

예를 들어, current가 “A”일 때

1. 길이가 5보다 작으므로 AA로 다시 DFS를 실행합니다.
2. AA→AAA→AAAA→AAAAA
3. AAAAA는 길이가 5이므로 종료하고 현재 값을 AAAA로 다시 자릅니다.
4. AAAA에서 E를 붙인 AAAAE로 DFS를 실행합니다.
5. AAAAE는 길이가 5이므로 AAAA로 다시 자르고 I를 붙인 AAAAI로 DFS를 실행합니다.

### 나의 풀이

```python
def dfs(current, dictionary, alpha_list):
    dictionary.append(current)
    for alpha in alpha_list:
        if len(current) != len(alpha_list):
            dfs(current+alpha, dictionary, alpha_list)
        else:
            current[:-1]

def solution(word):
    alpha_list = ['A','E','I','O','U']
    dictionary = []

    for i in range(len(alpha_list)):
        dfs(alpha_list[i], dictionary, alpha_list)

    return dictionary.index(word) + 1

```

### 배운 점

DFS를 이용해서 완전 탐색을 구현하는 방법에 조금 익숙해진 것 같습니다. 이번 구현에서는 DFS에서 자주 사용하는 return 문을 쓰지 않고 일정한 범위에서만 반복할 수 있도록 for문을 사용해서 풀이했습니다.

또한 위 과정을 itertools의 product를 이용해서 동일하게 구현할 수 있는 것을 알게 되었습니다. product(’ABCD’, repeat=2) = ‘AA’ ‘AB’ ‘AC ‘AD’ ‘BB’ … 등의 반복되는 문자들을 생성할 수 있습니다.

### 문제 설명

사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

### 제한사항

word의 길이는 1 이상 5 이하입니다.
word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.
