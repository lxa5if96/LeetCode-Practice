class Solution:
    def maxProduct(self, n: int) -> int:
        ans = []
        while ( n != 0):
            ans.append( n % 10)
            n = n // 10

        mx = 0
        seclarge = 0
        for i in ans:
            if i >= mx:
                seclarge = mx
                mx = i
            elif i > seclarge:
                seclarge = i

        mx * seclarge

        return mx * seclarge
        
