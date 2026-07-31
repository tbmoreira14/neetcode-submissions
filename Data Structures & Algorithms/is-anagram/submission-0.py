class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        tnew=sorted(t)
        snew=sorted(s)
        if(tnew == snew):
            return True
        return False