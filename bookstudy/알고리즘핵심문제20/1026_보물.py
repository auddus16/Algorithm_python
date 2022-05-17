import sys
N=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
b=list(map(int, sys.stdin.readline().split()))
a.sort(reverse=True)
b.sort()
tot=0
for i in range(N):
    tot+=a[i]*b[i]
print(tot)
