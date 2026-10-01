class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for b in s:
            if b =="(" or b =="[" or b =="{":
                ans.append(b)
            else:
                if not ans:
                    return False
                if ans[-1] != pairs[b]:
                    return False
                ans.pop()

        return len(ans) == 0