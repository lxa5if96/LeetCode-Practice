class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq  = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            a = len(nums) // 2
            if freq[num] > a:
                return num