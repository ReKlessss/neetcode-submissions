class Solution:
    def isValid(self, s: str) -> bool:
        p = {")": "(", "]": "[", "}": "{"}
        t = []

        for c in s:
            if c not in p:
                t.append(c)
            elif not t or t.pop() != p[c]:
                return False
        
        return not t
                