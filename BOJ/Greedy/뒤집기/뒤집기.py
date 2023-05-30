import sys

input = sys.stdin.readline

answer = 0
s = input()
convert_num = s
  
result = ''
for n in convert_num:
  if not result or result[-1] != n:
    result += n

print(min(result.count('0'), result.count('1')))