import sys
n = int(sys.stdin.readline().strip())
s = []
def back_tracking(idx):
    for i in range(1, (idx//2) + 1): # 좋은 수열인지 탐색
        if s[-i:] == s[-2*i:-i]: # 그렇지 않으면 -1 return
            return -1
    if idx == n: # 숫자 다 만들어졌으면, 출력하고 0 return
        print(''.join(map(str, s)))
        return 0

    for i in range(1, 4): # 다음 숫자 넣기
        s.append(i)
        if back_tracking(idx + 1) == 0: # 좋은 수열인지 recursion
            return 0
        s.pop()
back_tracking(0)