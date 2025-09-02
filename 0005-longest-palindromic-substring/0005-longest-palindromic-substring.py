class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        We know that base cases are

        * single letters are always palindromes
        * two letters are palindromes if s[i] == s[j]

        we can run through these base cases after we've set up our matrix
        """
        n = len(s)
        
        if n <= 1:
            return s
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_length = 1
        
        # single letters: Easier to initialise dp separately
        for i in range(n):
            dp[i][i] = True

        for j in range(1, n):
            for i in range(j):
                length = j - i + 1
                if s[i] == s[j]:
                    # Check the scenarios
                    if length <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                    # update matrix
                    if dp[i][j] and length > max_length:
                        max_length = length 
                        start = i
        
        return s[start: start + max_length]


        return s[j: i+1]
