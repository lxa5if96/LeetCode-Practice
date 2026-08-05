class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 :
            return 0
        elif x == 1 or x == 2:
            return 1

        for i in range(x):
            sr = i * i
            if sr == x:
                return i
            elif sr > x:
                return i - 1
        