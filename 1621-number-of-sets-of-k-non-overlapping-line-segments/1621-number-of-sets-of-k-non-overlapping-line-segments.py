class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        n = n + k - 1
        result = 1
        for i in range(1, 2 * k + 1):
            result = result * (n - i + 1) % MOD
            result = result * pow(i, MOD - 2, MOD) % MOD
        return result