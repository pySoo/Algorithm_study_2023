import sys
from itertools import combinations

input = sys.stdin.readline

answer = []
game = list(combinations(range(6), 2))

def check_round(round):
    global ans
    if round == 15:
        ans = 1
        for sub in result:
            if sub.count(0) != 3:
                ans = 0
                break
        return

    team1, team2 = game[round]
    for pos1, pos2 in ((0, 2), (1, 1), (2, 0)):
      if result[team1][pos1] > 0 and result[team2][pos2] > 0:
        result[team1][pos1] -= 1
        result[team2][pos2] -= 1
        check_round(round + 1)
        result[team1][pos1] += 1
        result[team2][pos2] += 1

for _ in range(4):
  data = list(map(int, input().split()))
  result = [data[i:i + 3] for i in range(0, 16, 3)]
  
  ans = 0
  check_round(0)
  answer.append(ans)

print(*answer)