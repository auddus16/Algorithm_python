import sys
a= ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s= sys.stdin.readline().strip()
res= 0
for i in s:
    for k in range(len(a)):
        if i in a[k]:
            res+= k+3
            break
print(res)
