t = int(input())

# 북, 동, 남, 서 (x, y)
directions = [[0,1], [1,0], [0,-1], [-1,0]]

def calculate_y(command, pos, dir):
  if command == 'F':
    return [a + b for a, b in zip(pos, dir)]
  elif command == 'B':
    return [a - b for a, b in zip(pos, dir)]

def calculate_x(command, dir):
  if command == 'L':
    next_idx = (directions.index(dir) + 1) % len(directions)
    return directions[next_idx]
  elif command == 'R':
    next_idx = (directions.index(dir) - 1 + len(directions)) % len(directions)
    return directions[next_idx]

def go_turtle(command_list):
  positions = []
  
  current_dir = directions[0]
  current_pos = [0,0]
  positions.append(current_pos)
  
  for command in command_list:
    if command == 'F' or command == 'B':
      current_pos = calculate_y(command, current_pos, current_dir)
      positions.append(current_pos)
      
    elif command == 'L' or command == 'R':
      current_dir = calculate_x(command, current_dir)

  max_x, max_y = 0, 0
  min_x, min_y = 0, 0
  
  for x,y in positions:
    max_x, max_y = max(max_x, x), max(max_y, y)
    min_x, min_y = min(min_x, x), min(min_y, y)
  
  height = abs(max_y) + abs(min_y)
  width = abs(max_x) + abs(min_x)  
  print(height * width)
  
for _ in range(t):
  go_turtle(list(input()))