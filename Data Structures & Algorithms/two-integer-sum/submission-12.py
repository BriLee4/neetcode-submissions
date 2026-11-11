class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create dictionary that has a compliment for each index
        #if compliment in nums return index
        #compliment = target - i

        res = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if nums[i] in res:
                return [res[nums[i]], i]
            res[comp] = i
