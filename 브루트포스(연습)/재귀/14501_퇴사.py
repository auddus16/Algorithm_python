import sys
N= int(sys.stdin.readline())
T, P= [], []
for _ in range(N):
    t, p= map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)
res=0
def go(i, total):
    global res
    if i == N:
        res= max(total, res)
        return
    if i > N:
        return
    go(i+1, total)
    go(i+T[i], total+P[i])

go(0, 0)
print(res)