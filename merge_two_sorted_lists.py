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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            if l1 is None:
                return l2
            if l2 is None:
                return l1
        else:
            new_list = LinkList()
            flag1 = True
            flag2 = True
            while (not (l1.next is None)) or (not (l2.next is None)):
                if l1.next is None:
                    if flag1:
                        if l1.val <= l2.val:
                            flag1 = False
                            new_list.append(l1.val)
                        else:
                            new_list.append(l2.val)
                            l2 = l2.next
                    else:
                        new_list.append(l2.val)
                        l2 = l2.next
                elif l2.next is None:
                    if flag2:
                        if l2.val <= l1.val:
                            flag2 = False
                            new_list.append(l2.val)
                        else:
                            new_list.append(l1.val)
                            l1 = l1.next
                    else:
                        new_list.append(l1.val)
                        l1 = l1.next
                else:
                    if l1.val <= l2.val:
                        new_list.append(l1.val)
                        l1 = l1.next
                    else:
                        new_list.append(l2.val)
                        l2 = l2.next
          
            if flag1 and flag2:
                if l1.val <= l2.val:
                    new_list.append(l1.val)
                    new_list.append(l2.val)
                else:
                    new_list.append(l2.val)
                    new_list.append(l1.val)
            elif flag1 and (not flag2):
                new_list.append(l1.val)
            elif (not flag1) and flag2:
                new_list.append(l2.val)

            return new_list.head


l1 = LinkList()
l2 = LinkList()
ele1 = [1]
ele2 = [3]
for e in ele1:
    l1.append(e)
for e in ele2:
    l2.append(e)
s = Solution()
n = s.mergeTwoLists(l1.head, l2.head)
while n:
    print 'value ', n.val
    n = n.next
