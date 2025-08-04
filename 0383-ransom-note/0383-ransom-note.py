from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        We need two counters, and then compare if magazine is a subset of ransomNote.

        Check that there is enough characters needed in magazine to generate ransom note.
        """
        rc = Counter(ransomNote)
        mc = Counter(magazine)

        for k, count in rc.items():
            if k not in mc:
                return False
            if mc[k] < count:
                return False
        
        return True


        