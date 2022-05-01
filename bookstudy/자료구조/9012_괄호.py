import sys
N=int(sys.stdin.readline().strip())
a=[sys.stdin.readline().strip() for _ in range(N)]
stk=[]
for i in range(N):
    flag = True
    stk.clear()
    for j in a[i]:
        if j == '(': # 여는 괄호
            stk.append('(')
        else:   # 닫는 괄호
            if len(stk) == 0: # 스택이 비어있을 경우 -> NO
                flag = False
                break
            else:
                stk.pop()

    if len(stk) != 0 or flag == False:
        print('NO')
    else:
        print('YES')
