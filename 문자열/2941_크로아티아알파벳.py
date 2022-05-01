import sys
input= sys.stdin.readline
s= input()
s= s.strip()
a= ['c=', 'c-', 'lj', 'nj', 'dz=', 'd-','s=', 'z=']

for i in a:
    s= s.replace(i, '*')

print(len(s))
