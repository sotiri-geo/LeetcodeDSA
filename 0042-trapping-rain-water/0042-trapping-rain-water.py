class Solution:
    def trap(self, height: List[int]) -> int:
        
        ans = 0
        stack = []

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                # top here represents the smallest value seen on stack
                top = stack[-1]
                stack.pop()
                if not stack:
                    break
                # distance between current (i) and next boundary
                dist = i - stack[-1] - 1
                # height is from comparing the floor from i - 1 to i - 2,3,...
                bounded_height = min(height[stack[-1]], height[i]) - height[top]

                ans += dist * bounded_height
            
            stack.append(i)
        
        return ans 