class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 #increment the letter freq in array
            res[tuple(count)].append(s) #for the count key append the word associated ot each key to the list
        return list(res.values())