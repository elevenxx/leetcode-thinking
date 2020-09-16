"""
input: an array of n positive integers and a positive interger s
output: the minimal length of a contiguous subarray of which the sum >= s;
        if there isn't one, return 0

sliding window tech
first using j pointer to expand the size of sliding window
then using i pointer to shrink the window
if there is a desiring result, compare it to the last desiring one,
because we want the minimum length of subarray
"""


def minLen(A, s):
    i, j, n = 0, 0, len(A)
    curSum, ans = 0, n+1
    while j < n:
        curSum += A[j]
        while curSum >= s:
            ans = min(ans, j-i+1)
            curSum -= A[i]
            i += 1
        j += 1
    if ans == n+1:
        return 0
    else:
        return ans


if __name__ == "__main__":
    nums = list(map(int, input().split(",")))
    s = int(input())
    ans = minLen(nums, s)
    print(ans)