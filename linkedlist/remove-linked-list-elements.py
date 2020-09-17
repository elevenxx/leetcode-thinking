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


# iterative
def removeElement(head, val):
    if not head: return head
    dummy = Node(-1)
    dummy.next = head
    cur = dummy
    while cur:
        if cur.next and cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


# recursive
def rem(head, val):
    if not head: return head
    head.next = rem(head.next, val)
    if head.val == val:
        return head.next
    else:
        return head


if __name__ == "__main__":
    mylist = SingleLinkList()
    for i in [1, 2, 3, 4, 6, 5, 6]:
        mylist.append(i)
    for i in mylist.traverse():
        print(i, end=' ')
    print("choose val you want to remove: ")
    val = int(input())
    p = rem(mylist._head, val)
    while p:
        print(p.val, end=' ')
        p = p.next
