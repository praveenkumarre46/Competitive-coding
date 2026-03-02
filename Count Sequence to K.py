from collections import Counter
from fractions import Fraction

class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mid = n // 2
        
        def get_all_outcomes(arr):
            outcomes = Counter({Fraction(1): 1})
            for x in arr:
                next_outcomes = Counter()
                for val, count in outcomes.items():
                    next_outcomes[val * x] += count
                    next_outcomes[val / Fraction(x)] += count
                    next_outcomes[val] += count
                outcomes = next_outcomes
            return outcomes

        left_side = get_all_outcomes(nums[:mid])
        right_side = get_all_outcomes(nums[mid:])
        
        total_sequences = 0
        target_k = Fraction(k)
        
        for left_val, left_count in left_side.items():
            needed_right = target_k / left_val
            if needed_right in right_side:
                total_sequences += left_count * right_side[needed_right]
                
        return total_sequences