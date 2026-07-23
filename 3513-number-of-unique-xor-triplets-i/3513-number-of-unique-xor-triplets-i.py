class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1 or l == 2:
            return l
        for i in range(l):
            a = 2 ** i
            if a > l:
                return a
        

