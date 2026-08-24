class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            if not self.alphaNum(s[lp]):
                lp += 1
                continue
            
            if not self.alphaNum(s[rp]):
                rp -= 1
                continue
            
            if s[lp].lower() != s[rp].lower():
                return False

            lp, rp = lp + 1, rp - 1
           

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))