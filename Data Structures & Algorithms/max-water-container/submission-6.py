class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, mArea = 0, len(heights) - 1, 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1
            mArea = max(mArea, area)
        return mArea