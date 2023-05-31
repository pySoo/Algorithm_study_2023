## CPU - 16506

[문제 링크](https://www.acmicpc.net/problem/16506)

### 구분

구현

### 풀이 요약

어셈블리어 코드를 주어진 규칙에 따라 기계어 코드로 변환하는 구현 문제였습니다. 명령어에 C가 붙어있느냐 아니냐에 따라서 비트 단위를 예외처리 해주는 것이 필요했습니다.

### 나의 풀이

```python
command_list = ['ADD', 'SUB', 'MOV', 'AND', 'OR', 'NOT', 'MULT', 'LSFTL', 'LSFTR', 'ASFTR', 'RL', 'RR']

n = int(input())
orders = []

def convert_to_binary(num, length):
  return str(bin(int(num))[2:]).zfill(length)

for _ in range(n):
  orders.append(list(input().split()))

for opcode, r1, r2, r3 in orders:
  is_inclue_c = False
  if opcode not in command_list:
    is_inclue_c = True
    opcode = opcode[:-1]

  command = convert_to_binary(command_list.index(opcode), 4)
  command += '1' if is_inclue_c else '0'
  command += '0'
  command += convert_to_binary(r1, 3)
  command += convert_to_binary(r2, 3)

  if is_inclue_c:
    command += convert_to_binary(r3, 4)
  else:
    command += convert_to_binary(r3, 3)
    command += '0'

  print(command)
```

### 배운 점

bin 메서드를 이용하여 값을 2진수로 변환하고 zfill을 이용해서 공백을 앞에서부터 메꾸는 방법에 대해서 알게 되었습니다. bin 메서드를 사용하면 ‘0bxxxxx’의 형태가 되기 때문에 앞의 문자열 두 개를 슬라이싱 하는 것이 필요했습니다.

그리고 점점 pythonic한 코드 작성에 익숙해지는 것 같습니다. python은 if else문을 이용하여 변수 값의 할당을 한 줄로 처리할 수 있습니다. 코드를 작성할 때는 편하지만 가독성에 크게 악영향을 준다면 지양하는 식으로 적절하게 판단하여 작성해야겠습니다.

### 문제 설명

디지털하드웨어설계 과목의 최종 프로젝트는 16-bit CPU를 설계하고 Verilog 언어로 구현하는 것이다. 본인이 구현한 CPU가 제대로 동작하는지 테스트하기 위해서는 기계어 코드를 입력으로 주어야 한다. 하지만 대부분의 사람은 0과 1로만 이루어진 기계어 코드를 이해하기 힘들어서 C++, Java와 같은 프로그래밍 언어로 코드를 작성하고 컴파일러를 통해 기계어 코드로 번역하는 과정을 거친다.

여러 가지 프로그래밍 언어 중에서 어셈블리어는 사람이 이해하기 쉬우면서 기계어와 가장 유사한 언어이다. 어셈블리어 코드는 어셈블러를 통해 기계어 코드로 번역된다. 그리고 어셈블리어는 기계어와 일대일로 대응하는 특징이 있다. 예를 들면, 두 수의 합을 구하는 연산의 어셈블리어 코드가 `ADD`이고, 기계어 코드가 `00000`이면 어셈블러는 `ADD`를 읽어서 그대로 `00000`로 바꾸어주는 것이다.

디지털하드웨어설계 과목을 듣는 민호는 Verilog로 16-bit CPU 구현을 일찍 끝내 놓은 상태이다. 이 16-bit CPU를 테스트하기 위해서는 기계어를 매번 입력으로 줘야 하는데, 너무나 귀찮은 민호는 이에 맞는 어셈블러를 구현하려고 한다. 민호가 직접 설계한 16-bit CPU의 명령어 구조 표를 보고, 어셈블리어 코드가 주어졌을 때 이를 기계어 코드로 번역하는 어셈블러를 만들어보자.

### 입력

첫 번째 줄에는 명령어의 개수를 의미하는 정수 *N* (1 ≤ *N* ≤ 500)이 주어진다.

다음 *N*개의 각 줄에는 명령어가 어셈블리어 코드로 *"opcode rD rA rB"* 또는 *"opcode rD rA #C"*의 형태로 주어진다. 문자열 *opcode*는 항상 대문자이다. 정수 *rD, rA, rB* (0 ≤ *rD, rA, rB* ≤ 7)는 레지스터 번호를 의미한다. 사용하는 레지스터 번호는 1부터 7까지이며, 사용하지 않을 경우에만 0이 주어진다. 정수 *#C* (0 ≤ *#C* ≤ 15)는 상수를 의미한다.

기계어 코드로 번역될 때 어긋나는 입력은 주어지지 않는다.

### 출력

*N*개의 각 줄에 어셈블리어 코드를 기계어 코드로 번역하여 출력한다.

### 예제 입력1

```python
4
MOVC 1 0 5
MOVC 2 0 10
ADD 3 1 2
SUB 4 1 2
```

### 예제 출력 1

```python
0010100010000101
0010100100001010
0000000110010100
0001001000010100
```
