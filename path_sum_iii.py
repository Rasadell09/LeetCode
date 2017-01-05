# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.cntResult(root, sum, [sum])

    def cntResult(self, node, origin, targets):
        if node is None:
            return 0

        hit = 0
        for t in targets:
            if t - node.val == 0:
                hit += 1
        targets = [t - node.val for t in targets] + [origin]
        return hit + self.cntResult(node.left, origin, targets) \
            + self.cntResult(node.right, origin, targets)
