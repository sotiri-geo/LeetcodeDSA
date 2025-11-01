class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        We need to define two maps to confirm the following:
        f X -> Y

        where f is both bijective and surjective
        """

        ST = {}
        TS = {}

        # We know both s and t are of the same length
        for i in range(len(s)):
            si = s[i]
            ti = t[i]

            # validate bijection
            if si in ST and ST[si] != ti:
                return False

            # validate surjection
            if ti in TS and TS[ti] != si:
                return False

            # acceptable to insert
            ST[si] = ti
            TS[ti] = si

        return True