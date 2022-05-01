import sys
board=list(list(map(int, sys.stdin.readline().split())) for _ in range(9))
empty=[(i, j) for i in range(9) for j in range(9) if board[i][j]==0]
def check(r,c):
    num=[1,2,3,4,5,6,7,8,9]
    for i in range(9): # 각 행, 열 검사
        if board[r][i] in num:
            num.remove(board[r][i])
        if board[i][c] in num:
            num.remove(board[i][c])
    r=(r//3)*3
    c=(c//3)*3
    for i in range(r, r+3):
        for j in range(c, c+3):
            if board[i][j] in num:
                num.remove(board[i][j])
    return num
def bt(cnt):
    if cnt==len(empty):#더 이상 0이 없음.
        for i in board:
            print(*i)
        sys.exit()
    (r, c)=empty[cnt] #다음 0의 위치 저장
    nums=check(r, c)
    for num in nums:
        board[r][c]=num
        bt(cnt+1)
        board[r][c]=0
bt(0)
