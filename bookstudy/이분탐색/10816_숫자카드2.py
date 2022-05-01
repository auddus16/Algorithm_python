from bisect import bisect_left, bisect_right
import sys
N= int(sys.stdin.readline())
card= list(map(int, sys.stdin.readline().split()))
M= int(sys.stdin.readline())
list_M= list(map(int, sys.stdin.readline().split()))

card.sort()
count= []

for i in list_M:
    s= bisect_left(card, i)
    e= bisect_right(card, i)
    count.append(e-s)
for i in count:
    print(i, end=' ')