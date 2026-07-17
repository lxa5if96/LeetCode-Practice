class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        sum = 0
        for i in range(l):
            sum += nums[i]
        
        total_sum = l *(l+1) // 2

        return  total_sum - sum
