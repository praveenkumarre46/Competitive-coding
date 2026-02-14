class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[[float('-inf')] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                dp[i][j][0] = 0

        for p in range(1, k + 1):
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    res = dp[i-1][j-1][p-1]
                    if res != float('-inf'):
                        dp[i][j][p] = max(dp[i][j][p], res + nums1[i-1] * nums2[j-1])
                    
                    dp[i][j][p] = max(dp[i][j][p], dp[i-1][j][p], dp[i][j-1][p])

        return dp[n][m][k]