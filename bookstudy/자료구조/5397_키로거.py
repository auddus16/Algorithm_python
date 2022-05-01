import sys
from collections import deque
for i in range(int(sys.stdin.readline().strip())):
    s = sys.stdin.readline().strip()
    pw_l = deque()
    pw_r = deque()
    for k in s:
        if k == '<':
            if len(pw_l):
                pw_r.appendleft(pw_l.pop())
        elif k == '>':
            if len(pw_r):
                pw_l.append(pw_r.popleft())
        elif k == '-':
            if len(pw_l):
                pw_l.pop()
        else:
            pw_l.append(k)

    print(''.join(pw_l)+''.join(pw_r))