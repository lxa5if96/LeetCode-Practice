
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, start, end):
            if lazy[node]:
                mid = (start + end) // 2
                val = lazy[node]

                tree[node * 2] += val * (mid - start + 1)
                tree[node * 2 + 1] += val * (end - mid)

                lazy[node * 2] += val
                lazy[node * 2 + 1] += val
                lazy[node] = 0

        def query(node, start, end, left, right):
            if right < start or end < left:
                return 0

            if left <= start and end <= right:
                return tree[node]

            push(node, start, end)
            mid = (start + end) // 2

            return (
                query(node * 2, start, mid, left, right)
                + query(node * 2 + 1, mid + 1, end, left, right)
            )

        def update(node, start, end, left, right):
            if right < start or end < left:
                return

            if left <= start and end <= right:
                tree[node] += end - start + 1
                lazy[node] += 1
                return

            push(node, start, end)
            mid = (start + end) // 2

            update(node * 2, start, mid, left, right)
            update(node * 2 + 1, mid + 1, end, left, right)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        last = {}
        current_sq = 0
        ans = 0

        for r, x in enumerate(nums):
            left = last.get(x, -1) + 1

            total = query(1, 0, n - 1, left, r)
            length = r - left + 1

            current_sq = (current_sq + 2 * total + length) % MOD

            update(1, 0, n - 1, left, r)

            ans = (ans + current_sq) % MOD
            last[x] = r

        return ans



        #copy paste 