import sys

n = int(sys.stdin.readline())
if n > 2:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    print(dp[-1])
else:
    print(n)
