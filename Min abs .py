class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        reversed_seen = {}
        min_dist = float('inf')
        
        for j, val in enumerate(nums):
            if val in reversed_seen:
                min_dist = min(min_dist, j - reversed_seen[val])
            
            rev_val = int(str(val)[::-1])
            reversed_seen[rev_val] = j
            
        return min_dist if min_dist != float('inf') else -1