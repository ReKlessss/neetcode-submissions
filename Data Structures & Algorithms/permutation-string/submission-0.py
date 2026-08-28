class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s1_c = [0] * 26 
        sw_c= [0] * 26
        l = 0

        for c in s1:
            s1_c[ord(c) - ord("a")] += 1
            
        for r in range(len(s2)):
            sw_c[ord(s2[r]) - ord("a")] += 1

            if (r - l + 1) > s1_len:
                sw_c[ord(s2[l]) - ord("a")] -= 1
                l += 1

            if sw_c == s1_c:
                return True

        return False
