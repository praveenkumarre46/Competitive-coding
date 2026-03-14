import sys

class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] == '1' else 0)
        
        memo = {}
        sys.setrecursionlimit(200000)

        def solve(start, length):
            state = (start, length)
            if state in memo:
                return memo[state]
            
            x = prefix[start + length] - prefix[start]
            
            if x == 0:
                res = flatCost
            else:
                res = length * x * encCost
            
            if length % 2 == 0:
                half = length // 2
                res = min(res, solve(start, half) + solve(start + half, half))
            
            memo[state] = res
            return res

        return solve(0, n)