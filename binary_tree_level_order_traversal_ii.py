# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def travel(node, lvl):
            if node is not None:
                tmp = [node.val]
                if len(res) <= lvl:
                    res.append(tmp)
                else:
                    res[lvl] += tmp
                travel(node.left, lvl + 1)
                travel(node.right, lvl + 1)

        travel(root, 0)
        res.reverse()
        return res


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print s.levelOrderBottom(root)
