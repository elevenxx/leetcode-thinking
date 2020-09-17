class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def traverse(self):
        cur = self._head
        while cur is not None:
            yield cur.val
            cur = cur.next

    def bulidlist(self, nums):
        dummy = cur = Node(-1)
        for i in range(len(nums)):
            cur.next = Node(nums[i])
            cur = cur.next
        return dummy.next

    def buildLinkList(self, nums, pos):
        dummy = cur = Node(-1)
        meet = None
        for i in range(len(nums)):
            cur.next = Node(nums[i])
            cur = cur.next
            if i == pos:
                meet = cur
        if meet:
            cur.next = meet
        return dummy.next


def hasCycle(head: Node) -> bool:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            print("This linked list has cycle.")
            return True
    print("This linked list has no cycle.")
    return False


if __name__ == "__main__":
    print("input list: ")
    nums = list(map(int, input().split(',')))
    p = SingleLinkList().buildLinkList(nums, 2)  # if 0 <= pos <= len(nums)-1, then has cycle
    hasCycle(p)
