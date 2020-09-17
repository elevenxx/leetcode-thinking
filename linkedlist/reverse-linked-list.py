"""
input: a singly linked list
output: reversed list of input

two pointer tech
1. use pre and cur to represent the node traversed before and now
2. while current node exists, then move pre and cur, pick the node pre points to,
    reverse it
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

# iterative
def reverseList(head):
    pre, cur = None, head
    while cur:
        temp = pre
        pre, cur = cur, cur.next
        pre.next = temp
    return pre

# recursive
def revList(head):
    if not head or not head.next:
        return head
    newh = revList(head.next)
    head.next.next = head
    head.next = None
    return newh



if __name__ == "__main__":
    mylist = SingleLinkList()
    for i in range(1, 6):
        mylist.append(i)
    print("original list")
    for i in mylist.traverse():
        print(i, end=' ')
    print("choose reverse method: iterative or recursive")
    t = input()
    if t == "iterative":
        print("reverse list, type = iterative")
        p = reverseList(mylist._head)
        while p:
            print(p.val, end=' ')
            p = p.next
    else:
        print("reverse list, type = recursive")
        p2 = revList(mylist._head)
        while p2:
            print(p2.val, end=' ')
            p2 = p2.next