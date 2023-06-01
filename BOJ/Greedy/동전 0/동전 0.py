import sys

input = sys.stdin.readline

n, k = map(int,input().split())
coins = []
answer = 0

for _ in range(n):
  coins.append(int(input()))  

for i in range(n-1, -1, -1):
  q, r = divmod(k, coins[i])
  answer += q
  k = r

print(answer)
    