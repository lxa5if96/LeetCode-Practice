class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = 0
        sl = 0
        for i in nums:
            if i > l:
                sl = l
                l = i
            elif i > sl:
                sl = i
            
        return (l - 1) * (sl - 1)