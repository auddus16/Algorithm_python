import sys
N=int(sys.stdin.readline())
a_value=list(map(int, sys.stdin.readline().split()))
a=[]
for i in range(N):
    a.append((i, a_value[i]))

a.sort(key=lambda x:x[1])
p=[0]*N
for i in range(N):
    p[a[i][0]]=i
print(' '.join(map(str, p)))