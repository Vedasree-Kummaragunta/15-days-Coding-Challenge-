class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        third = float('-inf')

        for num in reversed(nums):
            if num < third:
                return True
            while stack and num > stack[-1]:
                third = stack.pop()
            stack.append(num)

        return False
sol = Solution()
print(sol.find132pattern([1,2,3,4]))    
print(sol.find132pattern([3,1,4,2]))     
print(sol.find132pattern([-1,3,2,0]))    
