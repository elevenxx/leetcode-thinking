# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        use an array to store all nodes in the list
        """
        if not head:
            return
        
        vec = []
        node = head
        while node:
            vec.append(node)
            node = node.next
        
        i, j = 0, len(vec)-1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        
        vec[i].next = None
 
 
 
 
 class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        # step 1: find middle node
        # step 2: reverse the second half
        # step 3: merge two halves
        """
        
        if not head: return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    
    def mergeList(self, l1, l2):
        while l1 and l2:
            p1 = l1.next
            p2 = l2.next

            l1.next = l2
            l1 = p1

            l2.next = l1
            l2 = p2
