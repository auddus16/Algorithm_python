import sys
N=int(sys.stdin.readline())
S=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def go(idx, a, b):
    if idx==N:
        al=len(a)
        bl=len(b)
        if al<1 or bl<1:
            return -1
        sum_a=0
        sum_b=0

        for i in range(al):
            for j in range(al):
                if i==j:
                    continue
                sum_a+=S[a[i]][a[j]]

        for i in range(bl):
            for j in range(bl):
                if i==j:
                    continue
                sum_b += S[b[i]][b[j]]
        return abs(sum_a-sum_b)
    res=-1
    t1=go(idx+1, a+[idx], b)
    if res==-1 or (t1!=-1 and t1<res):
        res=t1
    t2=go(idx+1, a, b+[idx])
    if res==-1 or (t2!=-1 and t2<res):
        res=t2
    return res
print(go(0, [], []))