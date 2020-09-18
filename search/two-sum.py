nums = list(map(int, input().split()))
target = int(input())

nums.sort()
dic = {}
ans = None
for i, num in enumerate(nums):
    if target - num in dic:
         ans = [dic[target-num], i]
    dic[num] = i
print(ans)