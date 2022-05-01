import sys
N = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
val = [int(sys.stdin.readline().strip()) for _ in range(N)]
stk = []
for ch in s:
    if ch.isalpha():
        stk.append(val[ord(ch) - ord('A')])
    else:
        b = stk.pop()
        a = stk.pop()
        if ch == '+':
            stk.append(a+b)
        elif ch == '-':
            stk.append(a-b)
        elif ch == '*':
            stk.append(a*b)
        else:
            stk.append(a/b)
print(f'{stk[0]:.2f}')
