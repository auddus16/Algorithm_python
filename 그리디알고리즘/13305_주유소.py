import sys
N=int(sys.stdin.readline().strip())
L=list(map(int, sys.stdin.readline().split()))
C=list(map(int, sys.stdin.readline().split()))
minC=min(C)
sumL=sum(L)
price=0
for i in range(N-1):
    if C[i] == minC:
        price+= sumL*C[i]
        sumL=0
        break
    price+= L[i] * C[i]
    sumL-= L[i]
print(price)



