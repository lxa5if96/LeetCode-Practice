class Solution:
    def gcd(a,b)-> int:
        if a == 0:
            return b
        return gcd(b,a%b)

    def gcdSum(self, nums: list[int]) -> int:
        l = len(nums)
        mx = nums[0]
        sum = 0
        prefixGcd = []
        for i in range(l):
            a = nums[i]
            mx = max(mx,nums[i])
            b = gcd(mx , nums[i])
            prefixGcd.append(b)
        
        prefixGcd.sort()
        pl = len(prefixGcd)

        start = 0 
        end = pl - 1
        while(start < end):
            x = gcd(prefixGcd[start],prefixGcd[end])
            sum += x
            start += 1
            end -= 1


        return sum


