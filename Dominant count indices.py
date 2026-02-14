class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        total=sum(nums)
        n=len(nums)
        prevsum=0
        dominant=0
        for i in range(len(nums)):
            if nums[i]>((total-prevsum)/(n-i)):
                dominant+=1
            prevsum+=nums[i]
        return dominant
                
        