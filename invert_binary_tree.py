# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(node):
            if node is None:
                return None

            tmp = invert(node.left)
            node.left = invert(node.right)
            node.right = tmp
            return node
        return invert(root)

    def printTree(self, node):
        if node is None:
            return None
        print node.val
        self.printTree(node.left)
        self.printTree(node.right)


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.left.right = TreeNode(7)
s.printTree(root)
s.printTree(s.invertTree(root))

