from typing import List

class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, map = [], {}
        for i in nums2:
            while stack and stack[-1] < i:
                map[stack.pop()] = i
            stack.append(i)
        return [map.get(i, -1) for i in nums1]

class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, map = [], {}
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                map[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        return [map.get(i, -1) for i in nums1]
