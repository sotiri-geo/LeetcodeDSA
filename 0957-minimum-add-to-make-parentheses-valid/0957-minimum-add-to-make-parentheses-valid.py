class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        ()) -> 1 because we can remove the valid parenthesis and see how many off steps we have

        So we can take the length of the stack after we've popped off what is valid.
        """

        stack = []

        for p in s:
            if stack and stack[-1] == "(" and p == ")":
                stack.pop()
                continue

            stack.append(p)

        return len(stack)
        