class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {v: i for i, v in enumerate(nums)}
        swaps = 0
        for i in range(len(nums)):
            if nums[i] != target[i]:
                j = pos[target[i]]
                nums[i], nums[j] = nums[j], nums[i]
                pos[nums[j]] = j
                pos[nums[i]] = i
                swaps += 1

        return swaps
