# Definition for singly-linked list.
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        n = head
        while n is not None:
            tmp = n.next
            while tmp is not None:
                if n.val != tmp.val:
                    break
                n.next = tmp.next
                tmp = tmp.next
            n = n.next
        return head


s = Solution()
ele = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
ll = CreateList()
for e in ele:
    ll.append(e)
n = s.deleteDuplicates(ll.head)
while n:
    print 'val ', n.val
    n = n.next
