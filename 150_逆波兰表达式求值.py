from typing import List

class Solution(object):
    @staticmethod
    def evalRPN(self, tokens: List[int]) -> int:
        t = tokens.pop()
        if t in '+-*/':
            b, a = self.evalRPN(tokens), self.evalRPN(tokens)
            res = int(eval('a' + t + 'b'))
        else:
            res = int(t)
        return res
