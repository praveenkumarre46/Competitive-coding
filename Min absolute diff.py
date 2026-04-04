class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        res=101
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==1 and nums[j]==2:
                    res=min(res,abs(i-j))
                elif nums[j]==1 and nums[i]==2:
                    res=min(res,abs(i-j))
                    
        return res if res!=101 else -1