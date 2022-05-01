import sys
N=int(sys.stdin.readline())
a=list(int(sys.stdin.readline()) for _ in range(N))
dp=[0]*10001
dp[1]=a[0]
if N>1: # 런타임에러(index)
    dp[2]=a[0]+a[1]
for i in range(3, N+1):
    dp[i]=max(dp[i-1], dp[i-2]+a[i-1], dp[i-3]+a[i-1-1]+a[i-1])
print(dp[N])