import sys
N=int(sys.stdin.readline())
def getPrime(n):
    check= [False]*(n+1)
    prime= []
    for i in range(2, n+1):
        if not check[i]:
            prime.append(i)
            for k in range(i*2, n+1, i):
                check[k] = True
    return prime
a=[]
idx=0
prime=getPrime(N)
while True:
    if N==1:
        for i in a:
            print(i)
        break
    while N%prime[idx]==0:
        a.append(prime[idx])
        N//=prime[idx]
    idx+=1
