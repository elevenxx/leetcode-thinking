"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

输入：nums = [9,11], k = 2
输出：[11]

"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # deque 是滑动窗口，存放 nums 数组中进入滑动窗口的最大元素的下标位置 
        deque = collections.deque()
        ans = []

        # 遍历数组 nums
        for i, num in enumerate(nums):

            # 当窗口非空，且窗口大小超过 k，即 deque 队头元素值 小于等于 i-k 时，弹出队头元素
            if deque and deque[0] <= i-k:
                deque.popleft()

            # 当窗口非空，窗口中最后一个元素对应的 nums 数组值小于当前num 值时
            # 不断弹出 deque 队尾元素
            while deque and nums[deque[-1]] < num:
                deque.pop()
            
            # 当前元素最大，将下标存入 deque 中
            deque.append(i)

            # 当前窗口中有 k 个元素之后，将最大值存入 ans 中
            if i >= k-1:
                ans.append(nums[deque[0]])
        return ans
