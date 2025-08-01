class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Convert first to an char array then apply two pointers.
        Swap only when both are eng chars. Else move pointers closer.
        Recreating a string from char array is O(N).

        Time complexity: O(N)
        Space complexity: O(N)
        """
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            # need to only reverse if both are alpha chars
            if not s[left].isalpha():
                left += 1
            if not s[right].isalpha():
                right -= 1

            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                # shift
                left += 1
                right -= 1

        return "".join(s)

        