class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        for i, ch in enumerate(s,start=1):
            sum += (26 - (ord(ch) - ord("a"))) * i

        return sum