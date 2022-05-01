import sys
T= int(sys.stdin.readline())
for _ in range(T):
    H, W, N= map(int, sys.stdin.readline().split())
    floor= N % H
    ho = (N // H) + 1
    if floor ==0:
        floor= H
        ho-= 1
    print(floor*100+ho)