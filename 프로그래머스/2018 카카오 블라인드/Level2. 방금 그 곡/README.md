## [Level 2] 방금 그 곡 - 17683

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/17683)

### 구분

코딩테스트 연습 > 카카오 2018 블라인드 3차

### 풀이 요약

특정 문자들을 치환하여 부분 문자열을 비교하는 문제. 글자 수가 다른 '#'이 붙은 문자들을 치환한 다음 총 재생시간 동안 재생된 악보 문자열을 구해야 한다.

### 나의 풀이

```python
def replace_sharp(music):
    music = music.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return music

def get_diff_time(start, end):
    start_hour, start_min = map(int, start.split(':'))
    end_hour, end_min = map(int, end.split(':'))

    return (end_hour - start_hour) * 60 + end_min - start_min

def solution(m, musicinfos):
    answer = []
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        play_time = get_diff_time(start, end)

        music = replace_sharp(music)
        music_time = len(music)

        play_music = music * (play_time // music_time) + music[:play_time % music_time]

        if replace_sharp(m) in play_music:
            answer.append([play_time, title])

    if len(answer) == 0:
        return "(None)"

    else:
        answer = sorted(answer, key = lambda x: (-x[0]))
        return answer[0][1]
```

### 배운 점

문자를 토큰화 하는 법에 대해 익힐 수 있었다. 총 재생시간 동안 재생된 악보를 구하기 위해서는 나눗셈과 모듈러 연산을 통해 문자열을 슬라이싱 하면 된다. 정답 조건에 총 재생시간이 가장 길고, 먼저 재생된 것이 먼저라는 기준이 있으므로 sorted의 lambda 함수를 이용해서 총 재생시간(x[0])의 역수를 기준으로 정렬하도록 처리했다.

### 문제 설명

라디오를 자주 듣는 네오는 라디오에서 방금 나왔던 음악이 무슨 음악인지 궁금해질 때가 많다. 그럴 때 네오는 다음 포털의 '방금그곡' 서비스를 이용하곤 한다. 방금그곡에서는 TV, 라디오 등에서 나온 음악에 관해 제목 등의 정보를 제공하는 서비스이다.

네오는 자신이 기억한 멜로디를 가지고 방금그곡을 이용해 음악을 찾는다. 그런데 라디오 방송에서는 한 음악을 반복해서 재생할 때도 있어서 네오가 기억하고 있는 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다. 반대로, 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다. 그렇기 때문에 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다. 다음과 같은 가정을 할 때 네오가 찾으려는 음악의 제목을 구하여라.

방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
음악이 00:00를 넘겨서까지 재생되는 일은 없다.
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.

<h4>입력 형식</h4>
입력으로 네오가 기억한 멜로디를 담은 문자열 m과 방송된 곡의 정보를 담고 있는 배열 musicinfos가 주어진다.

m은 음 1개 이상 1439개 이하로 구성되어 있다.
musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로, 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다.

- 음악의 시작 시각과 끝난 시각은 24시간 HH:MM 형식이다.
- 음악 제목은 ',' 이외의 출력 가능한 문자로 표현된 길이 1 이상 64 이하의 문자열이다.
- 악보 정보는 음 1개 이상 1439개 이하로 구성되어 있다.

<h4>출력 형식</h4>
조건과 일치하는 음악 제목을 출력한다.

<h4>입출력 예제</h4>
<table>
        <thead><tr>
<th>m</th>
<th>musicinfos</th>
<th>answer</th>
</tr>
</thead>
        <tbody>
<tr>
<td>"ABCDEFG"</td>
<td>["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]</td>
<td>"HELLO"</td>
</tr>
</tbody>
      </table>
