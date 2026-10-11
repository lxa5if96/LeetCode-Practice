class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(1,isqrt(n) + 1):
            if n % i == 0:
                ans += nums[i-1] ** 2
                j = n // i
                if j != i:
                    ans += nums[j-1] ** 2
        return ans
