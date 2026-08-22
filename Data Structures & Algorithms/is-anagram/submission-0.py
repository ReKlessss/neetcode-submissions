class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # inputs: 2 strings of lowercase english letters with atleast 1 character
        
        # step 1: measure/compare the length of the strings
        # step 2: sort the strings -> e.g. sorted(s)
        # step 3: "".join(s) == "".join(t) 
        # step 4: check that they match
        
        # output: bool -> indicates whether the strings 

        if len(s) != len(t): return False

        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))

        if s_sorted == t_sorted:
            return True

        return False
