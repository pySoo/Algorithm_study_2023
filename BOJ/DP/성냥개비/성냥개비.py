t = int(input())

max_dp = [0] * 101
max_dp[2] = 1
max_dp[3] = 7

min_dp = [0, 0, 1, 7, 4, 2, 6, 8, 10]
min_dp.extend([float('inf')] * (101 - len(min_dp)))

arr = [0, 0, 1, 7, 4, 2, 0, 8]

for i in range(4, 101):
  max_dp[i] = int(str(max_dp[i - 2]) + '1')

for n in range(9, 101):
  for i in range(2, 8):
    min_dp[n] = min(min_dp[n], min_dp[n - i] * 10 + arr[i])


for _ in range(t):
  n = int(input())
  print(min_dp[n], max_dp[n])