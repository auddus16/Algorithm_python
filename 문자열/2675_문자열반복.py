import sys
input= sys.stdin.readline

T= int(input())
for t in range(T):
    n, s= map(str, input().split())
    n= int(n)
    for i in s:
        for k in range(n):
            print(i, end="")
    print()