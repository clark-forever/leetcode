from struct import TreeNode
from typing import List

class Solution1(object):
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # if root is None:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        res = []
        def helper(cur):
            if cur is None:
                return []
            res.append(cur.val)
            helper(cur.left)
            helper(cur.right)
        helper(root)
        return res

class Solution2(object):
    def preoderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, res = [], []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res

class Solution3(object):
    def preoderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur = root

        while cur:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right =None
                    res.append(cur.val)

        return res