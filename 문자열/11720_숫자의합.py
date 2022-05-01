import sys
input= sys.stdin.readline

n= int(input())
s= input()
res= 0
for i in range(n):
    res += int(s[i])
print(res)