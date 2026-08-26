class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        A = ord("a")

        for w in strs:
            temp = [0] * 26
            
            for l in w:
                i = ord(l) - A
                temp[i] += 1
            
            groups[tuple(temp)].append(w)

        return list(groups.values())

