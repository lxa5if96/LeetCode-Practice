class Solution:
    def maxProduct(self, n: int) -> int:
        digit = []
        while n:
            digit.append( n % 10)
            n //= 10

        digit.sort(reverse = True)
        return digit[0] * digit[1]