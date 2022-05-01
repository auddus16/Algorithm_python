import sys
l, c= map(int, sys.stdin.readline().split())
T= list(sys.stdin.readline().split())
res=[]
a=[]

T.sort()
print(T)
for i in T:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        a.append(i)

def go(cntA, cntB, s, i):
    if cntA+cntB == l:
        if cntA>=1 and cntB>=2:
            res.append(s)
            return
        else:
            return
    for k in range(i, len(T)):
        if T[k] in a:
            go(cntA+1, cntB, s+T[k], k+1)
        else:
            go(cntA, cntB+1, s+T[k], k+1)

go(0, 0, "", 0)
for i in res:
    print(i.strip())