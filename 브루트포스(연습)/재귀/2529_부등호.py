import sys
T= int(sys.stdin.readline())
a= list(map(str, sys.stdin.readline().split()))
a.insert(0, '')
mm=[False]*10
max=str(0)
min=str(sys.maxsize)

def go(idx, s):
    if len(s)==T+1:
        global max
        global min
        if int(max)<int(s):
            max=s
        if int(min)>int(s):
            min=s
            min=s.zfill(T+1)
        return -1

    if a[idx]=='>':
        k=int(s[-1])-1
        while k>=0:
            if not mm[k]:
                mm[k]=True
                go(idx+1, s+str(k))
                mm[k]=False
            k-=1
        return
    else:
        if a[idx]=='':
            k=0
        else:
            k=int(s[-1])+1
        while k<=9:
            if not mm[k]:
                mm[k]=True
                go(idx+1, s+str(k))
                mm[k]=False
            k+=1
        return
go(0, '')
print(max)
print(min)
