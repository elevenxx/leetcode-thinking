"""
input: an array
output: move all zeroes to the end of it
while maintaining the relative order of non-zero elements

two pointers tech
1. fast pointer traverses the array
2. slow pointer points to the non-zero elements
3. if current element, which is the fast pointer points to, is non-zero,
    then swap elements the two pointers point to, then move slow pointer;
    otherwise, do nothing
"""
def moveZero(A):
    fast, slow = 0, 0
    while fast < len(A):
        if A[fast] != 0:
            A[fast], A[slow] = A[slow], A[fast]
            slow += 1
        fast += 1

if __name__ == "__main__":
    nums = list(map(int, input().split(' ')))
    moveZero(nums)
    print(nums)
