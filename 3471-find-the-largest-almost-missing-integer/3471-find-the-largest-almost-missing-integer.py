class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = n - k + 1

        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = -1

        for x, indices in pos.items():
            total = 0
            left = right = None

            for i in indices:
                L = max(0, i - k + 1)
                R = min(i, m - 1)

                if L > R:
                    continue

                if left is None:
                    left, right = L, R
                elif L > right + 1:
                    total += right - left + 1
                    left, right = L, R
                else:
                    right = max(right, R)

            if left is not None:
                total += right - left + 1

            if total == 1:
                ans = max(ans, x)

        return ans