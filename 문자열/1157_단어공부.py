import sys
input= sys.stdin.readline

s= input()
s= s.strip()
arr= [0] * 26

for i in range(len(s)):
    if ord(s[i]) >= 97 :
        arr[ord(s[i])-97] += 1
    else:
        arr[ord(s[i])-65] += 1
check= 0
flag= True
for i in range(len(arr)):
    if check >=2:# 최대값이 여러개일 경우
        flag= False
        break
    if max(arr) == arr[i]:
        check+= 1
if flag:
    print(chr(arr.index(max(arr))+65))
else:
    print("?")