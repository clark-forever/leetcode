from typing import List
from struct import TreeNode

class Solution1:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(cur):
            if not cur:
                return
            helper(cur.left)
            res.append(cur.val)
            helper(cur.right)
        helper(root)
        return res

class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

class Solution3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur = root

        while cur:
            if not cur.left:
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
                    pre.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res
