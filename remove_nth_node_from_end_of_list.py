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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list_len = 0
        tmp_n = head
        while tmp_n.next:
            list_len += 1
            tmp_n = tmp_n.next
        list_len += 1

        if list_len == 1:
            return None
        else:
            idx = list_len - n
            if idx == 0:
                head = head.next
            else:
                n1 = head
                n2 = n1.next
                for i in xrange(idx - 1):
                    n1 = n1.next
                    n2 = n1.next

                n1.next = n2.next
            return head


s = Solution()
ele = [1, 2]
ll = CreateList()
for e in ele:
    ll.append(e)
n = s.removeNthFromEnd(ll.head, 1)
while n:
    print 'val ', n.val
    n = n.next
