class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if nums[i] in res:
                return [res.get(nums[i]), i]
            res[compliment] = i