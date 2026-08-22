class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        mostWater = 0

        while i < j:
            width = j - i
            cur_height = min(height[i], height[j])
            mostWater = max(mostWater, cur_height * width)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return mostWater
