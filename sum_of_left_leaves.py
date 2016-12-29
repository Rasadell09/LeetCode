# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumSingle(node, left):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                if left:
                    return node.val

            return sumSingle(node.left, True) + sumSingle(node.right, False)

        if root is None:
            return 0
        return sumSingle(root.left, True) + sumSingle(root.right, False)


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(7)
print s.sumOfLeftLeaves(root)
