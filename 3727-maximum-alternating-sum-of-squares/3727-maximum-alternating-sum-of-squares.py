class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(num * num for num in nums)
        mid = len(nums) // 2
        return sum(nums[mid:]) - sum(nums[:mid])