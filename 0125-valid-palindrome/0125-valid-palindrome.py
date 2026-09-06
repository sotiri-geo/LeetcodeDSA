class Solution:
    def isPalindrome(self, s: str) -> bool:
        # We need to convert all uppercase to lowercase
        parsed = []
        for char in s:
            if char.isalnum():
                parsed.append(char.lower())

        return parsed == parsed[::-1]        