from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # Remove indices outside the window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Remove smaller elements from the end
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Append the current max
            if i >= k - 1:
                result.append(nums[q[0]])

        return result
nums = [1,3,-1,-3,5,3,6,7]
k = 3
sol=Solution()
print(sol.maxSlidingWindow())