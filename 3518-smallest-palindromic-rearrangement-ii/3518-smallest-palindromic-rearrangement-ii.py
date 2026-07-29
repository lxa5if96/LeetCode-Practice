from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""

        for ch, cnt in freq.items():
            if cnt % 2:
                mid = ch
            half[ord(ch) - ord('a')] = cnt // 2

        LIMIT = k
        total = sum(half)

        def count(cnt):
            rem = sum(cnt)
            ans = 1

            for x in cnt:
                if x:
                    ans *= comb(rem, x)
                    if ans > LIMIT:
                        return LIMIT
                    rem -= x

            return ans

        if count(half) < k:
            return ""

        left = []

        while total:
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = count(half)

                if ways >= k:
                    left.append(chr(i + ord('a')))
                    total -= 1
                    break
                else:
                    k -= ways
                    half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]