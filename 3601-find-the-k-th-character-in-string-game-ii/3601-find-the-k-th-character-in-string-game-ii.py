class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        """
        We use the bit manipulation to figure out which transformation the kth 
        element is in. 

        we need to split the array into two halfs, left half and right half

        When k = 5, op = [0, 0, 0]

        left    right
        'aaaa | [a]aaa'

        if k = 2 ** t + a. When a != 0 in this case its 2 ** 2 + 1, then we know it lies
        on the right side. We need to use the bit_length to count the no. of transformations

        here k = 5 => 101 i.e. 3 bits i.e. in the 3rd transformation on the right side. To find its
        previous transformation it clearly came from the first value so we do k -= 1 << t => 1. We  
        stop.

        NOTICE if k = 4 how would this work

        left    right
        'aaa[a] | aaaa'

        Here k = 4 => 100 i.e. 3 bits would suggest the 3rd transformation, however its the last value
        of the prior transformation so it belongs in the 2nd transformation. Then we work backwards
        from there.

        """

        ans = 0

        while k != 1:
            t = k.bit_length() - 1
            if (k & k - 1 == 0):
                # if its a power of 2, the char we are looking at is in the prior transformation
                # so we reduce the bit length by 1 in order to deduct the correct transformation 
                # downstream
                t -= 1
            # This is key, we essentially mark the transformation t (by checking which bit it is (t))
            # and then deduct this off overal k
            k -= 1 << t
            if operations[t]:
                # Only accumulate the transformation if we've made a change to the char 
                # i.e. operation 1
                ans += 1
        # use all the accumulations found with operation 1 and reconstruct the kth element.    
        return chr(ord("a") + (ans % 26))
        