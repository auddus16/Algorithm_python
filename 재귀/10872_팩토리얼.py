import sys
N=int(sys.stdin.readline())
def facto(n):
    if n==0:
        return 1
    return facto(n-1)*n
print(facto(N))