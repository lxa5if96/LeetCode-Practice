class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        ans = []
        for i in range(len(digits)):
            sum = sum * 10 + digits[i] 

        
        incDigit = sum + 1

        while(incDigit != 0):
            rem = incDigit % 10
            ans.append(rem)
            incDigit = incDigit // 10
        
        reversed_list = ans[::-1]

        return reversed_list
        