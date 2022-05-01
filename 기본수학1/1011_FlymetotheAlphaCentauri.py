#이런 문제는 진짜 양심없다.
import sys, math
T= int(sys.stdin.readline())
for _ in range(T):
    x, y= map(int, sys.stdin.readline().split())
    res=0 #횟수
    dis=y-x #거리

    num= math.floor(math.sqrt(dis)) #루트n
    num_2= num ** 2 #n제곱
    inNum= math.sqrt(num_2) #증가시점

    if dis == num_2:#제곱수인 경우 2n-1
        res= num*2-1
    elif dis>num_2 and dis<num_2+inNum: #감소시점에 있는 경우 2n
        res= num*2
    elif dis>num_2+inNum: #증가시점에 있는 경우 2n+1
        res=num*2+1

    if dis < 4: #거리가 4보다 작은경우는 예외
        res= dis

    print(res)