class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        ans = []
        for i in range(len(nums)):
            c = min(a,b)
            for j in range (1, c + 1):
                if a % j == 0 and b % j == 0:
                    ans.append(j)

        return max(ans)