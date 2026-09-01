class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+ 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0) # get count for each number in nums set that to a key val pair in count
        for n, c in count.items(): #for each key val pair append the freq array to set index to count and value to the number
            freq[c].append(n)
        res = []
        for i in range(len(freq) -1, 0, -1): #traverse backwards thorugh freq array to get the highest frequesnce stop once we get the amount of frequencies needed
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res