class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq = {}
        for num in nums:
            if num in freq:
                return True
            else:
                freq[num] = 1
        return False

            
                