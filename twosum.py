from typing import List
class Solution:
    def two_sum(self,nums:List[int],target:int)->List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==target-nums[i]:
                    return [i,j]
nums=list(map(int,input("enter the numbers:").split()))
target=int(input("enter the target value:"))
sol=Solution()
print("value:",sol.two_sum(nums,target))