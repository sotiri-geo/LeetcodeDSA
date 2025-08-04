from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        By sorting each of the words, we can uniquely group them by their anagram
        """

        ans = defaultdict(list)

        for word in strs:
            # each anagram will be applied to the same key
            ans["".join(sorted(word))].append(word)

        return list(ans.values())

