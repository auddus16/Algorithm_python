import sys
s = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
stack = []
for i in s:
    stack.append(i)
    if i == stack[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

print(''.join(stack) if len(stack) else 'FRULA')

