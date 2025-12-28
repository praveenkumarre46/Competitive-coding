class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        opt1 = (need1 * cost1) + (need2 * cost2)
        
        op = min(need1, need2)
        if need1 > need2:
            opt2 = (op * costBoth) + ((need1 - need2) * cost1)
        else:
            opt2 = (op * costBoth) + ((need2 - need1) * cost2)
            
        opt3 = max(need1, need2) * costBoth
        
        return min(opt1, opt2, opt3)