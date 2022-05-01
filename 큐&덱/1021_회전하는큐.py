import sys
N, M=map(int, sys.stdin.readline().split())
m=list(map(int, sys.stdin.readline().split()))
a=[i+1 for i in range(N)]
b=0
c=0
for i in range(M):
    if a.index(m[i]) <= len(a)//2:
        while a[0]!=m[i]:
            a.append(a[0])
            del a[0]
            b+=1
    else:
        while a[0]!=m[i]:
            a.insert(0, a[-1])
            del a[-1]
            c+=1
    a.remove(a[0])
print(b+c)


