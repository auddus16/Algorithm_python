#완전탐색+스택
import sys
N, P=map(int, sys.stdin.readline().split())
arr=list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
stk=[[] for i in range(7)]
cnt=0
for i in arr:
    if len(stk[i[0]]) == 0:  # stack 비어있음.
        stk[i[0]].append(i[1])
        cnt += 1
    else:
        while len(stk[i[0]]) != 0:
            top = stk[i[0]][-1]
            if top < i[1]:  # p가 더 작은 경우-> push
                stk[i[0]].append(i[1])
                cnt += 1
                break
            elif top==i[1]: # p가 같은 경우-> 그냥 넘어감.
                break
            else:  # p가 더 큰 경우-> pop
                stk[i[0]].pop()
                cnt += 1
        if len(stk[i[0]]) == 0:  # stack 비어있음.
            stk[i[0]].append(i[1])
            cnt += 1
print(cnt)


