class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        The most straight forward solution would be to iterate through
        each string and keep track of the first value in each string.

        The prefix can only be as long as the shortest string.
        """
        size = min(len(s) for s in strs)
        ans = []

        for i in range(size):
            # Using first string as base
            candidate = strs[0][i] 

            for j in range(1, len(strs)):
                if strs[j][i] != candidate:
                    return "".join(ans)

            ans.append(candidate)
        return "".join(ans)