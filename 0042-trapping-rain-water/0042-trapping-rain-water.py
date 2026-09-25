class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l = []
        l.append(height[0])
        for i in range(1,n):
            l.append(max(l[i-1], height[i]))
            
        r= []
        r.append(height[n-1])
        for i in range(n-2,-1,-1):
            r.append(max(r[-1], height[i]))
        r.reverse()
        ans = 0
        for i in range(n-1):
            w = min(l[i],r[i])
            ans += w - height[i]
        return ans