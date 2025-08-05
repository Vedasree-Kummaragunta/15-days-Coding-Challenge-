from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1   # to handle case when prefix_sum == k

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]
            freq[prefix_sum] += 1

        return count
sol = Solution()
print(sol.subarraySum([1,1,1], 2))  
print(sol.subarraySum([1,2,3], 3))  
