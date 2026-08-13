class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] < 0:
                l = m + 1
            else:
                h = m - 1
        negative_count = l

        l = 0
        h = n - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] <= 0:
                l = m + 1
            else:
                h = m - 1
        positive_count = n - l
        
        return max(negative_count, positive_count)