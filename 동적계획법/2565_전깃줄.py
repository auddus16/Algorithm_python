import sys
N=int(sys.stdin.readline())
a=list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
dp=[0 for _ in range(N+1)]
a.sort(key=lambda x: x[0])
b=list(k[1] for k in a)
for i in range(N):
    for j in range(i):
        if b[j]<b[i] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(N-max(dp))