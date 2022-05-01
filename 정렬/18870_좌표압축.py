import sys
N=int(sys.stdin.readline())
x=list(map(int, sys.stdin.readline().split()))
x_=sorted(list(set(x)))
dic={x_[i]:i for i in range(len(x_))}
for i in x:
   print(dic[i],end=' ')