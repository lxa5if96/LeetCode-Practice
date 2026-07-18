import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s = min (nums)
        g = max (nums)
        return math.gcd(s,g)