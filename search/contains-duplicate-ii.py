import collections
nums = list(map(int, input().split()))
k = int(input())

#  nums[i] == nums[j] and |i-j| <= k
flag = False
dic = collections.defaultdict(list)
for i, num in enumerate(nums):
    dic[num].append(i)

for i in dic:
    pos = dic[i]
    if len(pos) >= 2:
        for j in range(1, len(pos)):
            if pos[j] - pos[j-1] <= k:
                flag = True
                break
    else:
        continue
print(flag)

