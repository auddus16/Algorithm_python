import sys
from itertools import permutations, combinations
N=int(sys.stdin.readline())
num=list(map(int, sys.stdin.readline().split()))
in_op=list(map(int,sys.stdin.readline().split()))
op=[]
for i in range(4):
    op.extend([i+1]*in_op[i])
ans=[-1e9, 1e9]
for i in set(permutations(op)):
    res= num[0]
    for k in range(0, N-1):
        if i[k]== 1:
            res+=num[k+1]
        elif i[k]==2:
            res-=num[k+1]
        elif i[k]==3:
            res*=num[k+1]
        else:
            if res<0:
                res=-(-res//num[k+1])
            else:
                res//=num[k + 1]
    ans[0]=max(ans[0], res)
    ans[1]=min(ans[1], res)
print(ans[0])
print(ans[1])

