import sys
N=int(sys.stdin.readline())
num=list(map(int, sys.stdin.readline().split()))
opN=list(map(int, sys.stdin.readline().split()))
n=[-1e9, 1e9] #이걸 내가 어떻게 알까요??????????뒤져????짜증나네
def bt(cnt, ans):
    if cnt==N-1:
        res=num[0]
        for i in range(0, N-1):
            if ans[i]==0:
                res+=num[i+1]
            elif ans[i]==1:
                res-=num[i+1]
            elif ans[i]==2:
                res*=num[i+1]
            else:
                if res<0:
                    res=-(res)
                    res//=num[i+1]
                    res=-(res)
                else:
                    res//=num[i+1]
        n[0]=max(n[0], res)
        n[1]=min(n[1], res)
        return
    for i in range(0, 4):
        if opN[i]==0:
            continue
        opN[i]-=1
        bt(cnt+1, ans+[i])
        opN[i]+=1
bt(0, [])
print(n[0])
print(n[1])