import sys
input=sys.stdin.readline

n= int(input())
a= list(map(int, input().split()))
a.sort()
res=0

def next_permutation():
    max=0
    for i in range(1, len(a)):
        if a[i-1]<a[i]:
            max=i
    if max==0:
        return -1
    for i in range(len(a)-1, max-1, -1):
        if a[i]>a[max-1]:
            a[i], a[max-1]= a[max-1], a[i]
            break
    b=a[max:]
    b.sort()
    a[max:]=b
    return a

next= a
while True:
    next= next_permutation()
    if next==-1:
        break
    sum=0
    for i in range(len(next)-1):
        sum+=abs(next[i]-next[i+1])
    if sum > res:
        res= sum
print(res)

