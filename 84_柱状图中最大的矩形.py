from typing import List

class Solution1:
    def largestRectangleArea(self, heights: List[int]):
        n = len(heights)
        left, right = [0] * n, [0] * n
        mono_stack = list()

        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
               mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i] - left[i] -1) * heights[i] for i in range(n)) if n else 0
        return ans


class Solution2:
    def largestRectangleArea(self, heights: List[int]):
        n = len(heights)
        left, right = [0] * n, [n] * n
        mono_stack = list()

        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n  else 0
        return ans