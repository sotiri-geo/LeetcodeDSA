import operator as op
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def div_truncate(a: int, b: int) -> int:
            q = abs(a) // abs(b)
            return -q if (a < 0) ^ (b < 0) else q
        op_by_id = {
            "+": op.add,
            "-": op.sub,
            "*": op.mul,
            "/": div_truncate,
        }

        stack = []

        for token in tokens:
            if token in op_by_id:
                # operator on stack 
                lst = int(stack.pop())
                fst = int(stack.pop())
                stack.append(op_by_id[token](fst, lst))
                continue 
            stack.append(token)
        # should be a single element
        return int(stack.pop())