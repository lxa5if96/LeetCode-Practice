class Solution:
    def maxArea(self, height: List[int]) -> int:
        i= 0 
        j = len(height) - 1
        maxWater= 0
        while(i < j):
            w = j - i
            h = min(height[i],height[j])
            maxWater = max(maxWater,w * h)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxWater