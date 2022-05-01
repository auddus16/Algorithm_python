import sys
N=int(sys.stdin.readline())
check=[0]*N #행
visited=[False]*N #열
cnt=0
def bt(r): #row
    global cnt
    if r==N:
        cnt+=1
        return
    for i in range(N):
        if visited[i]!=0:#i열에 퀸이 있는 경우
            continue
        check[r]=i #없는 경우 퀸을 놓는다.
        flag=True
        for k in range(r): #기존의 퀸들의 대각선 방향으로 겹치는 확인
            if abs(check[r]-check[k])==r-k:
                flag=False
                break
        if flag:
            visited[i]=True
            bt(r+1)
            visited[i]=False
bt(0)
print(cnt)
