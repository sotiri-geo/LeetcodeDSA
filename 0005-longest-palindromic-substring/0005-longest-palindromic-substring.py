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
        start, max_len = 0, 1

        # length = substring length
        for length in range(1, n + 1):      # from 1-char substrings to full length
            for i in range(n - length + 1):
                j = i + length - 1  # end index

                if s[i] == s[j]:
                    if length <= 2:   # "a" or "aa"
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                    if dp[i][j] and length > max_len:
                        start, max_len = i, length

        return s[start:start+max_len]
