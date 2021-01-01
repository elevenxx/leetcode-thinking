"""
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # prev 表示上一朵种植的花的位置，初始值为-1，表示没开始种花
        count, m, prev = 0, len(flowerbed), -1

        for i in range(m):
            # 遍历数组 flowerbed，遇到1时根据 prev 和当前位置 i，计算上一个区间内可以种植的花的最多数量
            # 然后令 prev=i，继续遍历数组剩下的元素
            if flowerbed[i] == 1:
                if prev < 0:
                    count += i // 2
                else:
                    count += (i - prev - 2) // 2
                if count >= n:
                    return True
                prev = i
        
        # 遍历数组flowerbed 结束后，计算最后一个区间内可以种植花的最多数量
        if prev < 0:
            count += (m + 1) // 2
        else:
            count += (m - prev - 1) // 2
        
        # 判断整个花坛可以种花的最多数量与 n 的大小关系
        return count >= n
