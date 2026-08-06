class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        ans = 1
        for digit in b:
            ans = pow(ans, 10, MOD)
            ans = (ans * pow(a, digit, MOD)) % MOD

        return ans