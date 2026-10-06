class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                ans.append(s[i])
            elif s[i] == ")":
                if ans[-1] == "(":
                    ans.pop()
                else:
                    ans.append(s[i])
            
        return len(ans) - 1
