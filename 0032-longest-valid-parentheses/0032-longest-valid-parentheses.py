class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = [-1]
        longest = 0

        for i in range(len(s)):
            if s[i] == "(":
                ans.append(i)

            else:
                ans.pop()

                if len(ans) == 0:
                    ans.append(i)
                    
                else:
                    count = i - ans[-1]
                    longest = max(longest, count)

        return longest