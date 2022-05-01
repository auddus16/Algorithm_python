import sys
N=int(sys.stdin.readline())
arr=list(sys.stdin.readline().strip())
s=[[0]*N for i in range(N)]
for i in range(N):
    for j in range(i, N):
        n=arr.pop(0)
        if n=='+':
            s[i][j]=1
        elif n=='-':
            s[i][j]=-1
res=[0]*N

def check(idx):
    sum=0
    for i in range(idx, -1, -1):
        sum+=res[i]
        if sum==0 and s[i][idx]!=0:
            return False
        elif sum<0 and s[i][idx]>=0:
            return False
        elif sum>0 and s[i][idx]<=0:
            return False
    return True

def go(idx):
    if idx==N:
        return True
    if s[idx][idx]==0:
        res[idx]=0
        return go(idx+1)
    for i in range(1, 11):
        res[idx]= s[idx][idx]*i
        if check(idx) and go(idx+1):
            return True
go(0)
print(' '.join(map(str, res)))
