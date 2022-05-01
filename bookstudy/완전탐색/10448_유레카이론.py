import sys
T = [n*(n+1)//2 for n in range(46)]
n = int(sys.stdin.readline())
for _ in range(n):
    a = int(sys.stdin.readline().strip())
    flag = False
    for i in range(1, 46):
        for j in range(i, 46):
            for k in range(j, 46):
                if T[i]+T[j]+T[k] == a:
                    flag = True
    if flag:
        print(1)
    else:
        print(0)