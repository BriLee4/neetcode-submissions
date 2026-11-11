class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs: #for each string in array make
            count = [0] * 26 #array of 26 length all assigned 0
            for c in s: # for each letter in each string
                count[ord(c) - ord('a')] += 1 #increment the array at position of ascii val of char
            res[tuple(count)].append(s)
        return list(res.values())