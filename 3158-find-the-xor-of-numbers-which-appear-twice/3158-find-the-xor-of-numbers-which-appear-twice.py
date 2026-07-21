class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans = [] 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    ans.append(nums[i])
                    break
        b = 0
        for num in ans:
            b ^= num
    
        return b