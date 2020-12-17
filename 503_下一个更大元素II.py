from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [-1] * len(nums)
        for i in range(2 * len(nums) - 1):
            while stack and nums[stack[-1] % len(nums)] < nums[i % len(nums)]:
                res[stack.pop() % len(nums)] = nums[i % len(nums)]
            stack.append(i)
        return res

class Solution2:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [-1] * len(nums)
        for i in range(2 * len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i % len(nums)]:
                stack.pop()
            if stack:
                res[i % len(nums)] = stack[-1]
            stack.append(nums[i % len(nums)])
        return res