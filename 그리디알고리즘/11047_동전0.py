import sys
N, K= map(int, sys.stdin.readline().split())
a=[int(sys.stdin.readline().strip()) for _ in range(N)]
cnt=0
for i in range(N-1, -1, -1):
    if a[i]<=K:
        cnt+=K//a[i]
        K%=a[i]
print(cnt)

