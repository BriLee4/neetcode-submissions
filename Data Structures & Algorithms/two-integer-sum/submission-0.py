class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numSet = {}
        n = len(nums)

        for i in range(n):
            compliment = target - nums[i]
            if compliment in numSet:
                return [numSet[compliment], i]
            numSet[nums[i]] = i
        return[]