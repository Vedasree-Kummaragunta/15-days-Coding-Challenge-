from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
nums = list(map(int,input("enter the numbers:").split()))
sol = Solution()
k = sol.removeDuplicates(nums)
print("count:",k)
print("Non-Duplicate list:",nums[:k])