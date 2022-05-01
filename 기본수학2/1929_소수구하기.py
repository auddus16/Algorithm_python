import sys
M, N= map(int, sys.stdin.readline().split())
check=[False]*(N+1)
prime=list()
def isPrime(n):
    for i in range(2, n+1):
        if not check[i]:
           prime.append(i)
        for k in range(i*2, n+1, i):
            check[k]=True
isPrime(N)
for i in prime:
    if i<M:
        continue
    print(i)