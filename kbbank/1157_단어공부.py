import sys
word = sys.stdin.readline().strip()
count = [0]*27
for s in word:
    idx = -1
    if 'a' <= s <= 'z':
        idx = ord(s) - 32 - ord('A')
    else:
        idx = ord(s) - ord('A')
    count[idx] += 1

maxV = max(count)
cnt = 0
flag = True
for i in count:
    if cnt >= 2:
        flag = False
        break
    if maxV == i:
        cnt += 1
if flag:
    print(chr(count.index(maxV)+65))
else:
    print('?')
