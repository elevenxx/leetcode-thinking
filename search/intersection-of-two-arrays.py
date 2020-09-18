nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
ans = set(nums1) & set(nums2)
print(ans)
