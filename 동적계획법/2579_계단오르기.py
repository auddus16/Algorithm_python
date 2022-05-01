import sys
N=int(sys.stdin.readline())
a=[0]*301 #런타임 에러 주의!
for i in range(1, N+1):
    a[i]=int(sys.stdin.readline())
dp=[0]*301
dp[1]=a[1]
dp[2]=a[1]+a[2]
for i in range(3, N+1):
    dp[i]=max(dp[i-3]+a[i-1]+a[i], dp[i-2]+a[i])
print(dp[N])