import sys
from itertools import permutations
input= sys.stdin.readline

n= int(input())
b= [i for i in range(n)]
a= [list(map(int, input().split())) for _ in range(n)] #2차원 배열 입력받기

cases= permutations(range(n))

res= sys.maxsize
for case in cases:
    if a[case[-1]][case[0]]== 0:
        continue
    sum=0
    flag= True
    for i in range(n-1):
        if a[case[i]][case[i+1]] == 0:
            flag= False
            break
        sum+= a[case[i]][case[i+1]]
        if sum >= res:
            flag= False
            break

    if not flag:
        continue
    sum+= a[case[-1]][case[0]]
    res= min(res, sum)

print(res)
