class Solution:
    def isValid(self, s: str) -> bool:
        """
        Use a stack to validate if a string has the correct open + closed braket

        With closed brackets we pop from top of stack.
        """


        closed_to_open = {")": "(", "]": "[", "}": "{"}

        stack = []

        for bracket in s:
            if not stack:
                if bracket in closed_to_open:
                    return False
                
                stack.append(bracket)

            else:
                top = stack[-1]
                if bracket in closed_to_open:
                    if top != closed_to_open[bracket]:
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(bracket)


        return len(stack) == 0