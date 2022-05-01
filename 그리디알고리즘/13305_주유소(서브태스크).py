import sys
N=int(sys.stdin.readline().strip())
L=list(map(int, sys.stdin.readline().split()))
C=list(map(int, sys.stdin.readline().split()))
minC=C[0]
price=0
#굳이 미리 sum을 구하지 않아도 된다 어차피 당장 움직여야하는 만큼 사야하기 때문
for i in range(N-1):
    if C[i]<minC:
        minC=C[i]
    price+=minC * L[i]
print(price)