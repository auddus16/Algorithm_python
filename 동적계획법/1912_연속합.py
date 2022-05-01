import sys
N=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
dp=[0]*N
dp[0]=a[0]
for i in range(1, N):
    dp[i]=max(dp[i-1]+a[i], a[i])
print(max(dp))

