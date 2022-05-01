import sys
T=int(sys.stdin.readline())

def getPrime(n):
    check=[True]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if check[i]:
            for j in range(i+i, n+1, i):
                check[j]=False
    return check

def go(prime, n):
    idx=0
    while True:
        if prime[n//2-idx] and prime[n//2+idx]:
            return (n//2-idx,n//2+idx)
        idx+=1
prime=getPrime(10001)
for _ in range(T):
    n=int(sys.stdin.readline())
    ans=go(prime, n)
    print("{} {}".format(ans[0], ans[1]))
