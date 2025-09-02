class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        We need to calculate each operation that gets us closer to the 
        value. 

        Base case is either answer or length < target word

        state variables
        
        i, j where i represents word1[i:]
        j represents word2[j:]

        Base cases 
        if i == len(word1) then we take all of word2[j:]
        if j == len(word2) then we delete rest of word1[i]

        w1 - h 
        w2 - r
        """ 
        @cache
        def dp(i, j):
            # base cases
            if i == len(word1):
                # At this point we assume that up to i we have the same
                # characters in word1 and word2. So we append rest of word2
                # at cost of len(word2) - j
                return len(word2) - j
            if j == len(word2):
                # remove unwanted chars from word 1
                return len(word1) - i

            if word1[i] == word2[j]:
                # skip
                return dp(i + 1, j + 1)
            # now we count the operations and take a min
            delete = dp(i + 1, j) + 1
            replace = dp(i + 1, j + 1) + 1
            insert = dp(i, j + 1) + 1 # make word2[j] appear in word1

            return min(delete, replace, insert)

        return dp(0, 0)
