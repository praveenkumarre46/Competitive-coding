class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        sub=set()
        for ele in s:
            sub.add(ele)
        mincost=float('inf')
        for ele in sub:
            submin=0
            for i in range(len(s)):
                if s[i]!=ele:
                    submin+=cost[i]
            mincost=min(mincost,submin)
        return mincost
                    
            
        
        