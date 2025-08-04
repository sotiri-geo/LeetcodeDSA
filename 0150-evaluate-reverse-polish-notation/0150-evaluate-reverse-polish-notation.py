class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Create a stack to compute operations in correct order.
        Once we reach an operand, we pop off the top two elements,
        apply the operand, then reappend the value to top of stack.

        Input should always be valid
        """ 

        operands = {"*", "-", "+", "/"}
        stack = []

        for token in tokens:
            if token in operands:
                snd = int(stack.pop())
                fst = int(stack.pop())
                if token == "*":
                    stack.append(fst * snd)
                elif token == "+":
                    stack.append(fst + snd)
                elif token == "-":
                    stack.append(fst - snd)
                elif token == "/":
                    stack.append(int(fst / snd))
            else:
                stack.append(token)

        return int(stack.pop())