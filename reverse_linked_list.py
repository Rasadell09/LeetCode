class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class CreateList(object):
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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def _reverse(node, prev=None):
            if node is None:
                return prev
            n = node.next
            node.next = prev
            return _reverse(n, node)
        return _reverse(head)
        # if head is None:
        #     return head
        # if head.next is None:
        #     return head
        # a = head
        # b = head.next
        # while b.next is not None:
        #     if a == head:
        #         a.next = None
        #     t = b.next
        #     b.next = a
        #     a = b
        #     b = t
        # if a == head:
        #     a.next = None
        # b.next = a
        # return b


s = Solution()
ele = [1]
ll = CreateList()
for e in ele:
    ll.append(e)
n = s.reverseList(ll.head)
while n:
    print 'val ', n.val
    n = n.next
