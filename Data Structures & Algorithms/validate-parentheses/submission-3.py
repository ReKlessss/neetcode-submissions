class Solution:
    def isValid(self, s: str) -> bool:
        p = {")": "(", "]": "[", "}": "{"}
        t = []

        for c in s:
            if c not in p:
                t.append(c)
            elif len(t) == 0 or p[c] != t[-1]:
                return False
            else:
                t.pop()
        
        return len(t) == 0
                