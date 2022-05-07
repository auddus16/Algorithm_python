import sys
from collections import deque
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
arr=[[False]*n for _ in range(n)]
for i in range(m): # 인접리스트 구성
    a, b= map(int, sys.stdin.readline().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
chk=[False]*n
def bfs(s):
    dq=deque()
    chk[s]=True
    dq.append(s)
    while dq:
        now=dq.popleft()
        for i in arr[now]: #인접한 노드는 모두 True
            if not chk[i]:
                chk[i]=True
                dq.append(i)
    return
bfs(0) #1번에 바이러스
print(chk.count(True)-1) #방문한 노드의 개수를 세어준다.


