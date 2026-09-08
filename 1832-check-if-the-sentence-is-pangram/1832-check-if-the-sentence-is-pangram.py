class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        We can use a set to manage state of chars.
        As the input constraint mentions only lowercase english letters
        we just need to assert on the lenght of the set being 26
        """
        return len({c for c in sentence}) == 26


        