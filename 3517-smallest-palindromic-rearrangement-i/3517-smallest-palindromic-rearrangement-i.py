class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        mid = n//2

        if n == 1:
            return s

        first_half= "".join(sorted(s[:mid]))

        if n % 2 == 0:
            return first_half + first_half[::-1]
        else:
            return first_half + s[mid] + first_half[::-1]


          