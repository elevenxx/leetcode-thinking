"""
input: an array
output: the m-th smallest element in an array

partition tech and recurse
1. the partition function returns the final position of pivot
2. return the desiring element or
    recurse the left or right part in the array depending on the result of 1.step
"""
import random


def findKth(A, l, r, m):
    if l >= r:
        return A[l]
    rp = random.randint(l, r)
    A[rp], A[l] = A[l], A[rp]
    j = partition(A, l, r)
    if j == m:
        return A[j]
    elif j > m:
        return findKth(A, l, j - 1, m)
    else:
        return findKth(A, j + 1, r, m)


# return the final position of A[l] in array
def partition(A, l, r):
    p = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1


if __name__ == "__main__":
    nums = list(map(int, input().split(",")))
    m = int(input())
    print(list(nums), m)
    ans = findKth(nums, 0, len(nums) - 1, len(nums) - m)  # k = len(nums)-m
    print(ans)  # the kth largest element in an array
    print(nums)  # partly sort the array because the partition function
