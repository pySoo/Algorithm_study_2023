from collections import deque

t = int(input())
answer = []
for _ in range(t):
  n, m = map(int, input().split())
  data = deque(map(int,input().split()))
  priority = deque()

  for idx, num in enumerate(data):
    priority.append((idx, num))

  print_num = 0
  while len(priority) > 0:
    idx, front = priority[0]
    max_num = max(priority, key=lambda x: x[1])[1]
    if front >= max_num:
      print_num += 1
      priority.popleft()
      if idx == m:
        break
    else:
      priority.popleft()
      priority.append((idx, front))
  
  answer.append(print_num)

for num in answer:
  print(num)