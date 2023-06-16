from collections import deque

n, w, L = map(int, input().split())
stack = deque(map(int, input().split()))

route = [0] * w

time = 0
while True:
  time += 1
  route = route[1:]
  route.append(0)

  if stack:
    if sum(route) + stack[0] <= L:
      route[-1] = stack.popleft()
  else:
    if sum(route) == 0:
      break
print(time)
