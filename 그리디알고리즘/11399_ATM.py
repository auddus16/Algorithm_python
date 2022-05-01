import sys
N=int(sys.stdin.readline().strip())
a=list(map(int, sys.stdin.readline().split()))
a.sort()
ans=0
for i in range(N):
    for j in range(i+1):
        ans+=a[j]
print(ans)

