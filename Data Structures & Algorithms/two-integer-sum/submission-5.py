class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            compliment = target - nums[i]
            if compliment in numMap:
                return [numMap[compliment], i]
            numMap[nums[i]] = i
        return[]