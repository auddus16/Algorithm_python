# 완전탐색
import sys
N, M= map(int, sys.stdin.readline().split()) # 행, 열
arr= list(sys.stdin.readline().strip() for _ in range(N))
ans=[]
for i in range(N-7):
    for j in range(M-7):
        start_b=0
        start_w=0

        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2==0: # n+m이 짝수인 경우
                    if arr[k][l] != 'B': #BWBW
                        start_b+=1
                    if arr[k][l] != 'W': #WBWB
                        start_w+=1
                else:
                    if arr[k][l] != 'W': #BWBW
                        start_b+=1
                    if arr[k][l] != 'B': #WBWB
                        start_w+=1
        ans.append(min(start_w, start_b))
print(min(ans))



