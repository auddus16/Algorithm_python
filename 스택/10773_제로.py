import sys
K=int(sys.stdin.readline().strip())
a=list(sys.stdin.readline().strip() for _ in range(K))
b=[]
for i in a:
    if i=='0':
        b.pop()
    else:
        b.append(int(i))
print(sum(b))