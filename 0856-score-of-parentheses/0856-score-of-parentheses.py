class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = [0] 
        for i in range(len(s)):
            if s[i] == "(":
                ans.append(0)
            else:
                a = ans.pop()
                if a == 0:
                    a = 1
                else:
                    a = 2 * a
                
                ans[-1] += a
            
        
        return ans[0]
