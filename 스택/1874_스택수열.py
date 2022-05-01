import sys

n= int(sys.stdin.readline().strip())
res= [int(sys.stdin.readline().strip()) for _ in range(n)]
stack=[]
ans=[]

i= 0
flag= True

for k in res:
    while i<k:
        i+=1
        stack.append(i)
        ans.append('+')
    if stack[-1]>=k:
        stack.pop()
        ans.append('-')
    else:
        flag=False
if flag:
    for k in ans:
        print(k)
else:
    print('NO')