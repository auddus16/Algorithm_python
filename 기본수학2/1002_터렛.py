import sys, math
T=int(sys.stdin.readline())
for _ in range(T):
    x1,y1,r1,x2,y2,r2=map(int, sys.stdin.readline().split())
    dis=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if dis==0 and r1==r2:
        print(-1)
    elif dis==r1+r2 or dis==abs(r1-r2):
        print(1)
    elif dis<r1+r2 and dis>abs(r1-r2):
        print(2)
    else:
        print(0)