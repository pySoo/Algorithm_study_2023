t = int(input())
operator = [' ','+','-']
result = []

def recursive(now, answer):
  if now == n + 1:
    calculate(answer)
    return
  for o in operator:
    recursive(now+1, answer+o+str(now))

def calculate(answer):
  replaced = answer.replace(' ', '')
  if eval(replaced) == 0:
    print(answer)
  
  
for i in range(t):
  n = int(input())
  recursive(2, '1')
  print()