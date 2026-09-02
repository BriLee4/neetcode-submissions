class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create hashmap Key is an array that holds frequency of characters. values is count of
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())