class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        s_original = str(n)
        
        fact_map = {
            '0': 1, '1': 1, '2': 2, '3': 6, '4': 24, 
            '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880
        }
        
        total_sum = 0
        for char in s_original:
            total_sum += fact_map[char]
            
        s_sum = str(total_sum)
        
        if len(s_sum) != len(s_original) or s_sum[0] == '0':
            return False
            
        return sorted(s_original) == sorted(s_sum)