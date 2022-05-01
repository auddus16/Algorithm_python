import sys
N=int(sys.stdin.readline())
map=[[' ' for i in range(N)] for i in range(N)]
def star(n):
    global map
    if n==3:
        map[0][:3]= map[2][:3]=['*']*3
        map[1][:3]= ['*', ' ', '*']
        return
    a=n//3
    star(n//3)
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            for k in range(a):
                map[a*i+k][a*j:a*(j+1)]=map[k][:a]
star(N)
for i in map:
    for j in i:
        print(j, end='')
    print()