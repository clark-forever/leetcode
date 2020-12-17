from typing import List

class Solution1:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        mins = [nums[0]]
        for i in nums[1:]:
            mins.append(min(i, mins[-1]))
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > mins[i]:
                while stack and mins[i] >= stack[-1]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False

class Solution2:
    def find132pattern(self, nums: List[int]) -> bool:
        third = float('-inf')
        stack = []
        for num in reversed(nums):
            if third > num:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        return False

