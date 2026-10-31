class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        ans = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans = [];
        for num, count in sorted_freq[:k]:
            ans.append(num)

        return ans