class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:  #words in list
            count = [0] * 26
            for c in s: #characters in word
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s) #key is the count array s is the word
        return list(res.values())