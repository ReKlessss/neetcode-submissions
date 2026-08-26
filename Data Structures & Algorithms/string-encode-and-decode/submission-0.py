class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            p = f"{len(strs[i])}#"
            res += f"{p}{strs[i]}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0

        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1


            c = int(s[l:r])
            w = s[r + 1: r + c + 1]
            l = r + c + 1
            res.append(w)

        return res



