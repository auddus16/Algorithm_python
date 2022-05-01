#순열 라이브러리 사용
import sys
from itertools import permutations

input= sys.stdin.readline
n= int(input())
a= list(map(int, input().split()))

cases= list(permutations(a))

res=0
for case in cases: #가능한 모든 순열들 중 하나씩 계산하여 차이의 최대값 구하기
    sum=0
    for i in range(n-1):
        sum+= abs(case[i]-case[i+1])
    res= max(res, sum)

print(res)
