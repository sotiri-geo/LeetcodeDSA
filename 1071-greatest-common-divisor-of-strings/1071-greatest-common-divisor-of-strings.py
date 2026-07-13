import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # We need to find all the divisors of len(str1)
        # and len(str2)
        size1 = len(str1)
        size2 = len(str2)
        ans = ""

        def divisor(num, a, b):
            return (a % num == 0) and (b % num == 0)

        for i in range(0, min(size1, size2)):
            num = i + 1
            if not divisor(num, size1, size2):
                continue
            
            div1 = size1 // num
            div2 = size2 // num
            
            cand1 = str1[:num] * div1
            cand2 = str2[:num] * div2 
            

            if (cand1 == str1) and (cand2 == str2) and (str1[:num] == str2[:num]):
                ans = str1[:num]


        return ans


