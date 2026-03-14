class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        limit = 10**14 + 7
        suffix_prod = [1] * n
        for i in range(n - 2, -1, -1):
            val = suffix_prod[i + 1] * nums[i + 1]
            suffix_prod[i] = val if val < limit else limit
            
        current_left_sum = 0
        for i in range(n):
            if current_left_sum == suffix_prod[i]:
                return i
            current_left_sum += nums[i]
            
        return -1