class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        ans = []
        seen = set()
        parsed = []

        for original in transactions:
            name, time, amount, city = original.split(",")

            # Remove dups
            parsed.append((name, int(time), int(amount), city, original))

        n = len(parsed)
        for i in range(n):
            for j in range(n):
                if i == j:
                    # ignore the same transaction
                    continue
                # focus on evaluating current transaction
                curr_name, curr_time, curr_amount, curr_city, curr_orig = parsed[i]
                next_name, next_time, next_amount, next_city, _ = parsed[j]

                if curr_amount > 1000 and i not in seen:
                    ans.append(curr_orig)
                    seen.add(i)
                    continue
                
                if curr_name == next_name and curr_city != next_city and abs(curr_time - next_time) <= 60 and i not in seen:
                    ans.append(curr_orig)
                    seen.add(i)

        return ans
                

        

        