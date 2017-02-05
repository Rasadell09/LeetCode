# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cnt = collections.Counter()
        def dfs(node):
            cnt[node.val] += 1
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)

        if root is not None:
            dfs(root)
        else:
            return []
        max_ct = max(cnt.itervalues())
        return [k for k, v in cnt.iteritems() if v == max_ct]