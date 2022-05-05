import sys
from itertools import combinations

N, M= map(int, sys.stdin.readline().split())
city= list(sys.stdin.readline().split() for _ in range(N))
home=[]
chick=[]
for i in range(N):
    for j in range(N):
        if city[i][j]=='2':
            chick.append((i, j))
        elif city[i][j]=='1':
            home.append((i, j))
ans=[]
for i in combinations(chick, M):
    total_h=0
    for h in home:
        minV=2*N+1
        for c in i:
            minV=min(minV, abs(h[0]-c[0])+abs(h[1]-c[1]))
        total_h+=minV
    ans.append(total_h)

print(min(ans))