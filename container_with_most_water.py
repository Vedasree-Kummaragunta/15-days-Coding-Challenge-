from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Width between lines
            width = right - left
            # Height is limited by the shorter line
            min_height = min(height[left], height[right])
            # Area = width * height
            max_area = max(max_area, width * min_height)

            # Move the pointer of the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
height = [1,8,6,2,5,4,8,3,7]
