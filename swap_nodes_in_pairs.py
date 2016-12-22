# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            n = ListNode(data)
            self.head = n
        else:
            n = self.head
            while n.next:
                n = n.next

            new_node = ListNode(data)
            n.next = new_node


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h, h.next = self, head
        #h.next = head
        while h.next and h.next.next:
            a = h.next
            b = a.next
            h.next, b.next, a.next = b, a, b.next
            h = a
        return self.next
        # pre, pre.next = self, head
        # while pre.next and pre.next.next:
        #     a = pre.next
        #     b = a.next
        #     pre.next, b.next, a.next = b, a, b.next
        #     pre = a
        # return self.next


s = Solution()
ele = [1, 2, 3, 4, 5]
ll = LinkList()
for e in ele:
    ll.append(e)
n = s.swapPairs(ll.head)
while n:
    print 'val ', n.val
    n = n.next
