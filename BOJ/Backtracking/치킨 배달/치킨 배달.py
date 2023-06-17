n, m = map(int, input().split())
board = []
chicken = []
home = []

for i in range(n):
  board.append(list(map(int, input().split())))
  for j in range(n):
    if board[i][j] == 1:
      home.append((i, j))
    elif board[i][j] == 2:
      chicken.append((i, j))


def caculate_distance(path1, path2):
  return abs(path1[0] - path2[0]) + abs(path1[1] - path2[1])


def get_chicken_distance(path):
  chicken_distance = 0
  for i in range(n):
    for j in range(n):
      if board[i][j] == 1:
        home_path = (i, j)
        distance = float('inf')
        for chicken_path in path:
          distance = min(distance, caculate_distance(chicken_path, home_path))
        chicken_distance += distance
  return chicken_distance


def dfs(depth, path):
  global answer
  if len(path) == m:
    distance = get_chicken_distance(path)
    answer = min(answer, distance)
    return

  if depth == len(chicken):
    return
  dfs(depth + 1, path + [chicken[depth]])
  # 백트래킹
  dfs(depth + 1, path)


answer = float("inf")

dfs(0, [])

print(answer)