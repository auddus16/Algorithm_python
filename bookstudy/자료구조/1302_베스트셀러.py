import sys
N = int(sys.stdin.readline().strip())
dic = dict()
for i in range(N):
    title = sys.stdin.readline().strip()
    if title in dic:
        dic[title] += 1
    else:
        dic[title] = 1

max = max(dic.values())
arr = []
for k, v in dic.items():
    if v == max:
        arr.append(k)
arr.sort()
print(arr[0])