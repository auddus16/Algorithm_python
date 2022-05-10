import sys
N=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
ans=[-1]*N
stk=[]
for i in range(0, N):
    while stk and arr[i]>stk[-1][1]:
        ans[stk[-1][0]]=arr[i]
        stk.pop()
    stk.append((i, arr[i]))
print(' '.join(map(str, ans)))