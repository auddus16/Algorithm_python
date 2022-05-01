import sys
input= sys.stdin.readline

s= input()
s= s.strip() #문자열 양 옆 공백제거 해야함.
res= [-1]*26

for i in range(len(s)):
    if res[ord(s[i])-ord('a')] == -1:
        res[ord(s[i])-ord('a')]= i
    else:
        continue
for i in res:
    print(i, end=' ')