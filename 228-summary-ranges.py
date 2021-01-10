"""
给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b
 

示例 1：

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/summary-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        n = len(nums)
        ans = []
        start = nums[0]

        # 为了方便处理最后一个元素，这里复制最后一个元素加入数组
        nums.append(nums[-1])

        for i in range(n):
            if nums[i+1] == nums[i] + 1:
                continue
            else:
                if start != nums[i]:
                    ans.append(str(start) + "->" + str(nums[i]))
                else:
                    ans.append(str(start))
                start = nums[i+1]
            
        return ans
