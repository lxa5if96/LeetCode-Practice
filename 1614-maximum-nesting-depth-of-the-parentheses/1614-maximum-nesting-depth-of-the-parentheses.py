class Solution:
    def maxDepth(self, s: str) -> int:
        ans = []
        c = 0
        max_depth = 0
        for i in range(len(s)):
            if s[i] == "(":
                ans.append(s[i])
                c += 1
                
                max_depth = max(c,max_depth)
                
            elif s[i] == ")":
                ans.pop()
                c -= 1
            
        return max_depth