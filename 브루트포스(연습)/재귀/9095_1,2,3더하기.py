import sys
T= int(sys.stdin.readline())
t= [int(sys.stdin.readline()) for i in range(T)]

def go(sum, goal):
    if sum>goal:#실패
        return 0
    if sum==goal:#성공
        return 1
    res=0;
    for i in range(1, 4):
        res+=go(sum+i, goal)
    return res

for i in t:
    print(go(0, i))