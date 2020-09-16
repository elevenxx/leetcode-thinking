"""
input: a sorted array, a specific target number
output: the indices of the two numbers such that they add up to the target

use a dictionary to store the mapping from numbers to their indices
"""


def twoSum(A, target):
    dic = {}
    for i, num in enumerate(A):
        if target - num in dic:
            return [dic[target - num] + 1, i + 1]
        dic[num] = i


if __name__ == "__main__":
    nums = list(map(int, input().split(",")))
    t = int(input())
    ans = twoSum(nums, t)
    print(ans)