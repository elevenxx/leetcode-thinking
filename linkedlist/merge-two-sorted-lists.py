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


def merge(l1: Node, l2: Node) -> Node:
    cur = dummy = Node(-1)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1; l1 = l1.next
        else:
            cur.next = l2; l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dummy.next


if __name__ == "__main__":
    l1 = SingleLinkList()
    l2 = SingleLinkList()
    print("input list 1: ")  # 1, 2, 3, 4, 5, 10
    a1 = list(map(int, input().split(',')))
    print("input list 2: ")  # 2, 5, 6, 7, 12
    a2 = list(map(int, input().split(',')))
    for i in a1:
        l1.append(i)
    for i in a2:
        l2.append(i)
    print("original list 1 and list 2: ")
    for i in l1.traverse():
        print(i, end=' ')
    print()
    for i in l2.traverse():
        print(i, end=' ')
    print()
    print("merge list")
    p = merge(l1._head, l2._head)
    while p:
        print(p.val, end=' ')
        p = p.next