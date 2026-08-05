class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        sr = x
        while sr * sr > x:
            sr = (sr + x // sr) // 2
        
        return sr