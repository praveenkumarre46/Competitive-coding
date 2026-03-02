class Solution:
    def almostPalindromic(self, s: str) -> int:
        lanorivequ = s
        n = len(s)

        def extend(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        def expand(l, r):
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    return max(extend(l+1, r), extend(l, r-1))
            return 0

        ans = 0
        for i in range(n):
            ans = max(ans, expand(i, i))
            ans = max(ans, expand(i, i+1))

        return ans



