from typing import List

class Solution1:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        max_right = [0] * n
        max_right[-1] = height[-1]
        for i in range(n - 1, 1, -1):
            max_right[i - 1] = max(max_right[i], height[i - 1])
        res = 0
        cur = height[0]
        for i in range(1, n - 1):
            cur = max(height[i], cur)
            res += min(cur, max_right[i]) - height[i]
        return res

class Solution2:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left, right = 0, n - 1
        res = 0
        max_left, max_right = height[0], height[-1]
        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1
        return res

class Solution3:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack:
                    break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i - stack[-1] - 1)
            stack.append(i)
        return res
            

class Solution4:
    def trap(self, height: List[int]) -> int:
        lmax, rmax, res = 0, 0, 0
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[i])
            res += lmax + rmax - height[i]
        return res - lmax*len(height)
