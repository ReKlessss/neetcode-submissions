class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for w in strs:
            temp = [0] * 26
            
            for l in w:
                i = ord(l) - ord("a")
                temp[i] += 1
            
            groups[tuple(temp)].append(w)

        return list(groups.values())

