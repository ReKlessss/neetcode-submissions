class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sort_w = "".join(sorted(word))

            if sort_w in anagrams:
                anagrams[sort_w].append(word)
            else:
                anagrams[sort_w] = [word]

        return list(anagrams.values())

        

