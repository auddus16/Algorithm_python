import sys
N=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
dp=[0]*N
dp[0]=1
for i in range(1, N):
    dp[i]=1
    for j in range(0, i):
        if a[j]<a[i]:
            dp[i]=max(dp[i], dp[j]+1)
print(max(dp))