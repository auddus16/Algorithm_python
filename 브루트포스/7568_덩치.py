import sys
N=int(sys.stdin.readline())
a=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
res=[]
for i in a:
    k=0
    for j in a:
        if i[0]<j[0] and i[1]<j[1]:#덩치크다.
            k+=1
    res.append(k+1)
print(' '.join(map(str,res)))