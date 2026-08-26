class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']

        if len(ones) < k:
            return ""

        best_left = 0
        best_right = len(s)

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            curr_len = right - left + 1
            best_len = best_right - best_left + 1
            
            if curr_len < best_len:
                best_left = left
                best_right = right

            elif curr_len == best_len:
                if s[left:right + 1] < s[best_left:best_right + 1]:
                    best_left = left
                    best_right = right

        return s[best_left:best_right + 1]