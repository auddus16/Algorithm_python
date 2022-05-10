import sys
from itertools import permutations
arr=sys.stdin.readline().strip()
ans='Z'*50
for i in set(permutations(arr)):
    print(i)
    flag=True
    for k in range(len(arr)//2):
        if i[k]!=i[len(arr)-1-k]:
            flag=False
            break
    if flag:
        if ans>''.join(i):
            ans=''.join(i)
if not len(ans):
    print("I'm Sorry Hansoo")
else:
    print(ans)
