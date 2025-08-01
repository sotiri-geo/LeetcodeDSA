class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = cost = ans = 0
        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))

            # constraint invalid
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            # valid
            ans = max(ans, right - left + 1)

        return ans

        