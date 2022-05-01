import sys
N, K= map(int, sys.stdin.readline().split())
a= [i for i in range(1, N+1)]
res=[]
idx=0
for i in range(N):
    idx+=K-1
    idx%=len(a)
    res.append(a.pop(idx))

print(f"<{', '.join(map(str, res))}>")