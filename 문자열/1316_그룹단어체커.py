import sys
T= int(sys.stdin.readline())
words= [sys.stdin.readline().strip() for i in range(T)]
res= 0
for word in words:
    check=[0]
    flag= True
    for i in word:
        if check[-1] == i:
            continue
        else:
            if i in check:
                flag= False
                break
            else:
                check.append(i)
    if flag:
        res+=1
print(res)