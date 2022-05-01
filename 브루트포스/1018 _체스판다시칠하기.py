import sys
N,M=map(int,sys.stdin.readline().split())
ch=[list(map(str,sys.stdin.readline().strip())) for _ in range(N)]
cnt=[]
for i in range(N-7):
    for j in range(M-7):
        black=0 #검흰검흰---
        white=0 #흰검흰검---
        for k in range(i, i+8):
            for n in range(j, j+8):
                if (k+n)%2==0: #홀짝은 끼리끼리 같은 색
                    if ch[k][n] !='W':
                        white+=1
                    if ch[k][n] !='B':
                        black+=1
                else:
                    if ch[k][n] != 'W':
                        black += 1
                    if ch[k][n] != 'B':
                        white += 1
        cnt.append(min(black, white))
print(min(cnt))

