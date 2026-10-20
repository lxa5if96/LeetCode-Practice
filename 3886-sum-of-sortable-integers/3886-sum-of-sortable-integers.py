from typing import List
from math import isqrt

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        divisors = []
        for k in range(1, isqrt(n) + 1):
            if n % k == 0:
                divisors.append(k)
                if k != n // k:
                    divisors.append(n // k)

        for k in divisors:
            possible = True
            prev_max = float("-inf")

            for start in range(0, n, k):
                block = nums[start:start + k]
                drops = 0
                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        drops += 1

                if drops > 1:
                    possible = False
                    break
                    
                block_min = min(block)
                block_max = max(block)

                if prev_max > block_min:
                    possible = False
                    break

                prev_max = block_max

            if possible:
                ans += k

        return ans