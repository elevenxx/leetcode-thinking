"""
input: an arbitrary array 0, 1, 2 represent three different colors
output: same color are adjacent, with the order of 0, 1, 2

three pointer tech
1. three pointer left, mid, right point to 0, 1, 2 respectively
2. mid pointer traverse the array from the begin to the position where it meets right pointer
3. if mid points to 0, then swap elements that mid and left point to, and move mid and left forward;
    if mid points to 1, only move mid pointer forward;
    if mid points to 2, then swap elements that mid and right point to, and only move right pointer backward
"""
def sortColors(A):
    left, mid, right = 0, 0, len(A)-1
    while mid <= right:
        if A[mid] == 0:
            A[mid], A[left] = A[left], A[mid]
            mid += 1
            left += 1
        elif A[mid] == 1:
            mid += 1
        else:
            A[mid], A[right] = A[right], A[mid]
            right -= 1

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    sortColors(nums)
    print(nums)