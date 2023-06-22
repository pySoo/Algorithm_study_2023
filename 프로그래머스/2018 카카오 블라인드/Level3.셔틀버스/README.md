## 셔틀버스 - 17678

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/17678)

### 구분

구현, 문자열

### 풀이 요약

시간들을 문자열 처리를 통해서 계산하고 주어진 간격에 맞춰서 버스에 탈 수 있는 인원을 배치하는 구현 문제였습니다. 문자열을 정수로 바꿔주고 시간을 비교하거나 정수로 바꾼 시간을 다시 정해진 양식의 문자열로 변환해야하기 때문에 문자열 처리가 복잡했던 문제였습니다.

### 나의 풀이

```python
from collections import defaultdict

def caculate_bus_time(index, t):
    time_int = 9 * 60 + index * t
    return convert_int_to_time(time_int)

def convert_time_to_int(time):
    hour, minute = list(map(int, time.split(':')))
    return hour * 60 + minute

def convert_int_to_time(time_int):
    hour, minute = divmod(time_int, 60)
    return str(hour).zfill(2) + ':' + str(minute).zfill(2)

def is_before_time(prev, after):
    prev = convert_time_to_int(prev)
    after = convert_time_to_int(after)
    if after >= prev:
        return True
    else:
        return False

def solution(n, t, m, timetable):
    answer = ''
    bus_dict = defaultdict(list)
    timetable.sort()

    for index in range(n):
        bus_time = caculate_bus_time(index, t)
        bus_dict[bus_time] = []
        pop_index = -1
        for time_index,time in enumerate(timetable):
            if is_before_time(time, bus_time):
                if len(bus_dict[bus_time]) < m:
                    bus_dict[bus_time].append(time)
                    pop_index = time_index
        if pop_index > -1:
            timetable = timetable[pop_index+1:]

    bus_key = list(bus_dict.keys())
    if bus_key:
        final_bus = bus_dict[bus_key[-1]]
        if len(final_bus) == m:
            time_int = convert_time_to_int(final_bus[-1]) - 1
            return convert_int_to_time(time_int)
        else:
            return bus_key[-1]

    return answer
```

### 배운 점

python의 **문자열 슬라이싱과 문자열 변환**에 익숙해진 것 같습니다. 특히나 시간의 경우 문자열을 파싱해서 정수로 변환해주는 것이 중요한데, 자주 사용되는 코드는 함수로 묶어서 처리해주는 것이 가독성 면에서도 좋고 오류를 디버깅하기에도 좋은 것 같습니다.

### 문제 설명

카카오에서는 무료 셔틀버스를 운행하기 때문에 판교역에서 편하게 사무실로 올 수 있다. 카카오의 직원은 서로를 '크루'라고 부르는데, 아침마다 많은 크루들이 이 셔틀을 이용하여 출근한다.

이 문제에서는 편의를 위해 셔틀은 다음과 같은 규칙으로 운행한다고 가정하자.

- 셔틀은 `09:00`부터 총 `n`회 `t`분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 `m`명의 승객이 탈 수 있다.
- 셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다. 예를 들어 `09:00`에 도착한 셔틀은 자리가 있다면 `09:00`에 줄을 선 크루도 탈 수 있다.

일찍 나와서 셔틀을 기다리는 것이 귀찮았던 콘은, 일주일간의 집요한 관찰 끝에 어떤 크루가 몇 시에 셔틀 대기열에 도착하는지 알아냈다. 콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하여라.

단, 콘은 게으르기 때문에 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다. 또한, 모든 크루는 잠을 자야 하므로 `23:59`에 집에 돌아간다. 따라서 어떤 크루도 다음날 셔틀을 타는 일은 없다.

### **입력 형식**

셔틀 운행 횟수 `n`, 셔틀 운행 간격 `t`, 한 셔틀에 탈 수 있는 최대 크루 수 `m`, 크루가 대기열에 도착하는 시각을 모은 배열 `timetable`이 입력으로 주어진다.

- 0 ＜  `n` ≦ 10
- 0 ＜  `t` ≦ 60
- 0 ＜  `m` ≦ 45
- `timetable`은 최소 길이 1이고 최대 길이 2000인 배열로, 하루 동안 크루가 대기열에 도착하는 시각이 `HH:MM` 형식으로 이루어져 있다.
- 크루의 도착 시각 `HH:MM`은 `00:01`에서 `23:59` 사이이다.

### **출력 형식**

콘이 무사히 셔틀을 타고 사무실로 갈 수 있는 제일 늦은 도착 시각을 출력한다. 도착 시각은 `HH:MM` 형식이며, `00:00`에서 `23:59` 사이의 값이 될 수 있다.
