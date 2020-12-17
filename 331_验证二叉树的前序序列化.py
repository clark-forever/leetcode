class Solution1:
    res = True
    i = 0

    def helper(self):
        if self.i >= len(self.preorder):
            self.res = False
            return
        self.i += 1
        if self.preorder[self.i - 1] == '#':
            return
        self.helper()
        self.helper()

    def isValidSerialization(self, preorder: str) -> bool:
        self.preorder = preorder.split(',')
        self.helper()
        return self.i == len(self.preorder) and self.res

class Solution2:
    def isValidSerialization(self, preorder: str) -> bool:
        edges = 1

        for node in preorder.split(','):
            edges -= 1
            if edges < 0:
                return False
            if node != '#':
                edges += 2

        return edges == 0


import re
class Solution3:
    def isValidSerialization(self, preorder: str) -> bool:
        l = len(preorder)
        while True:
            preorder = re.sub(r'[0,9]+,#,#', '#', preorder)
            if l == len(preorder):
                break
            l = len(preorder)
        return '#' == preorder