"""
给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例：

输入：head = 1->4->3->2->5->2, x = 3
输出：1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        # 维护两个链表，small 链表顺序存储所有小于 x 的节点，large 链表存储所有大于等于 x 的节点
        small, large = ListNode(-1), ListNode(-1)
        smallHead, largeHead = small, large

        # 遍历链表
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        
        # 遍历结束
        # large 链表尾节点指向空，small 链表尾节点指向 large 头结点
        large.next = None
        small.next = largeHead.next
        return smallHead.next
