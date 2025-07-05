class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        
        for ch in s:
            if ch == "R":
                balance += 1
            else:
                balance -= 1
                
            # in check when 0
            if balance == 0:
                count += 1
                
        return count