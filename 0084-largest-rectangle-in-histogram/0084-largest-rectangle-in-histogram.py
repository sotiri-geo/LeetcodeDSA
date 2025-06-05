class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Mono dec stack where when we violate and pop from stack
        we compute area.

        Width is determind by the stack and height is current popped element.
        """

        # stack stores indexes
        stack = []
        ans = 0
        n = len(heights)

        for i in range(n + 1):
            # dummy height at end
            curr_height = 0 if i == n else heights[i]
            # mono inc stack, i.e. pop when you know its less than top of stack
            
            while stack and heights[stack[-1]] > curr_height:

                idx = stack.pop()
                height = heights[idx]

            
                width = i if not stack else i - stack[-1] - 1

                ans = max(ans, height * width)
        

            stack.append(i)

        return ans


        