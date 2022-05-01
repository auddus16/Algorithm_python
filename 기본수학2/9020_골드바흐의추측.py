import sys
T=int(sys.stdin.readline())

def isPrime(n):
    check = [False] * (n + 1)
    prime = []
    for i in range(2, n + 1):
        if not check[i]:
            prime.append(i)
            for k in range(i * 2, n + 1, i):
                check[k] = True
    return prime
def go(a, res, idx):
    if len(a)==2:
        if res==n:
            if (a[1]-a[0]) < (ans[1]-ans[0]):
                ans[0], ans[1]= a[0], a[1]
            else:
                return
        else:
            return
    for i in range(idx, len(prime)):
        if prime[i]+res>n:
            return
        a.append(prime[i])
        go(a, res+prime[i], i)
        a.remove(prime[i])

for _ in range(T):
    n=int(sys.stdin.readline())
    check=[False]*(n+1)
    prime=list()
    isPrime(n)
    ans=[0, sys.maxsize]
    go([], 0, 0)
    for i in ans:
        print(i, end=" ")
    print()



