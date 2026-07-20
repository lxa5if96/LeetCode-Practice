import math
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dis = math.inf
        ans = math.inf
        for i in range(len(nums)):
            if abs(nums[i]) < dis:
                ans = nums[i]
                dis = abs(ans)

            elif abs(nums[i]) == dis and nums[i] > ans:
                ans = nums[i]



        return ans
                