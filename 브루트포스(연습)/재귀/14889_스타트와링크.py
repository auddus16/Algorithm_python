import sys
N= int(sys.stdin.readline())
S=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def go (idx, a, b):
    if idx==N:
        if len(a)!=N//2 or len(b)!=N//2:#불가능
            return -1
        #팀원 분배완료!
        sum_a=0
        sum_b=0
        for i in range(N//2):
            for j in range(N//2):
                if i==j:
                    continue
                sum_a+=S[a[i]][a[j]]
                sum_b+=S[b[i]][b[j]]
        return abs(sum_a-sum_b) #능력치 차이 리턴
    if len(a)>N//2 or len(b)>N//2:#불가능
        return -1
    res=-1
    t1= go(idx+1, a+[idx], b)
    if res==-1 or (t1!=-1 and t1<res):
        res=t1
    t2= go(idx+1, a, b+[idx])
    if res==-1 or (t2!=-1 and t2<res):
        res=t2
    return res

print(go(0, [], []))