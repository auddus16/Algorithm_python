import sys
N = int(sys.stdin.readline().strip())
t, p = [], []
for i in range(N):
    T, P = map(int, sys.stdin.readline().strip().split())
    t.append(T)
    p.append(P)

dp = [0] * (N+1)

M = 0
for i in range(N):
    M = max(M, dp[i])
    if i+t[i] > N:
        continue
    dp[i+t[i]] = max(M+p[i], dp[i+t[i]])

print(max(dp))