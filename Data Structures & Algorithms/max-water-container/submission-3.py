class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxA = 0
        while r > l:
            area = (r - l) * min(heights[l], heights[r])
            maxA = max(maxA, area)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return maxA