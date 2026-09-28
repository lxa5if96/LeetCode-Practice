class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        c = 0
        for ch in s:
            if ch == "(":
                c += 1
                ans = max(ans,c)
            elif ch ==")":
                c -= 1
                
        return ans