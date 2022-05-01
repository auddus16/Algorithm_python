import sys
T=int(sys.stdin.readline().strip())
a=list(sys.stdin.readline().strip() for _ in range(T))
for i in a:
    b=[]
    flag=True
    for k in i:
        if k==')':
            if len(b)==0:#닫는 괄호가 있는데, 스택은 비어있는 경우 -> NO
                flag=False
                break
            b.pop()
        elif k=='(':
            b.append('(')
    if len(b)!=0:#문자열이 끝났는데, 스택이 비어있지 않은 경우
        flag=False
    if flag:
        print('YES')
    else:
        print('NO')