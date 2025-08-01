class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        
        for i in range(len(word)):
            if word[i] == ch:
                index = i + 1
                break
        # No such ch
        if index == -1:
            return word

        left = word[:index]
        right = word[index:]
        return left[::-1] + right
        
        