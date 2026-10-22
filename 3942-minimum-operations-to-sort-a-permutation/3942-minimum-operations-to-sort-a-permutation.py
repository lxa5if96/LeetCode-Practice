class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        def find_rotation(arr):
            k = arr.index(0)
            for i in range(n):
                if arr[(k + i) % n] != i:
                    return -1
                    
            return k

        ans = float('inf')

        # Case 1: Rotate the original array
        k = find_rotation(nums)
        if k != -1:
            ans = min(ans, min(k, n - k + 2))

        # Case 2: Reverse and rotate
        k = find_rotation(nums[::-1])
        if k != -1:
            ans = min(ans, min(k, n - k) + 1)

        return ans if ans != float('inf') else -1