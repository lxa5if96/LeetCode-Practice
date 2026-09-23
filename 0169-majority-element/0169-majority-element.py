class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = 1
        maj = nums[0]
        for i in range(1,len(nums)):
            if c == 0:
                maj = nums[i]
                c = 1
            elif nums[i] == maj:
                c += 1
            else:
                c -= 1

        return maj