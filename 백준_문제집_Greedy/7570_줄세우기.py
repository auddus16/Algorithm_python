import sys
n = int(sys.stdin.readline().rstrip("\n"))
nums = list(map(int, sys.stdin.readline().rstrip("\n").split()))
nums.insert(0,0)
positions=[0]*(n+1)
for i in range(1,len(nums)):
    positions[nums[i]] = i
count=1
max=-1
for i in range(1,len(nums)-1):
    if(positions[i] < positions[i+1]): # 이동 안 해도 되는 경우
        count+=1
        if(count>max):
            max = count
    else:
        count=1

print(n-max if n != 1 else 0)