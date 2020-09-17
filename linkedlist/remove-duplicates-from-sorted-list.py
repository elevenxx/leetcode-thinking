"""
see if the next node's value is equal to current node's
if yes, then skip next node
if no, just move forward
"""
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

    def append(self, item):
        node = Node(item)
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node


def deleteDuplicates(head):
    cur = head
    while cur:
        if cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


if __name__ == "__main__":
    mylist = SingleLinkList()
    print("input: ")
    inputlist = list(map(int, input().split(',')))
    for i in inputlist:
        mylist.append(i)
    print("original list")
    for i in mylist.traverse():
        print(i, end=' ')
    print()
    print("remove duplicates")
    p = deleteDuplicates(mylist._head)
    while p:
        print(p.val, end=' ')
        p = p.next