class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            current_sum = 0
            elements_in_subarray = set()
            
            for j in range(i, n):
                current_sum += nums[j]
                elements_in_subarray.add(nums[j])
                
                if current_sum in elements_in_subarray:
                    count += 1
                    
        return count