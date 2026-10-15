class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0 
        n = len(nums)  
        for i in range(n):
            seenNum = set()
            for j in range(i,n):
                seenNum.add(nums[j])
                distinct = len(seenNum)
                ans = ans + distinct * distinct
        return ans