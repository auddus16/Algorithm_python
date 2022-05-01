import sys
N=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
dp=[0]*N
dp[0]=a[0]
for i in range(1, N):
    for j in range(0, i):
        if a[j]<a[i]:
            dp[i]=max(dp[j], dp[i])
    dp[i]+=a[i]
print(max(dp))