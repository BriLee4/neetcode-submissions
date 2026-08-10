class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxA = 0
        for i in range(n):
            for j in range(i +1, n):
                if heights[i] < heights[j]:
                    area = heights[i] * (j - i)
                    maxA = max(area, maxA)
                else:
                    area = heights[j] * (j - i)
                    maxA = max(area, maxA)
        return maxA