# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth = []
        q = []
        q.append(root)
        depth.append(1)
        max_d = 0
        while len(q) != 0:
            if max_d < max(depth):
                max_d = max(depth)
            n = q.pop()
            lv = depth.pop()
            if n.right:
                q.append(n.right)
                depth.append(lv + 1)
            if n.left:
                q.append(n.left)
                depth.append(lv + 1)
        return max_d


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print s.maxDepth(root)
