class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        minaveloru = nums
        
        dic = {}
        for ele in minaveloru:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        
        secfreq = {}
        for val in dic.values():
            if val in secfreq:
                secfreq[val] += 1
            else:
                secfreq[val] = 1
        
        for ele in minaveloru:
            if secfreq[dic[ele]] == 1:
                return ele
                
        return -1