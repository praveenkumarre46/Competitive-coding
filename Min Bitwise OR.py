class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        ans = 0
        
        for bit in range(30, -1, -1):
            target = ans | ((1 << bit) - 1)
            
            is_possible = True
            for row in grid:
                row_has_valid_num = False
                for val in row:
                    if (val | target) == target:
                        row_has_valid_num = True
                        break
                
                if not row_has_valid_num:
                    is_possible = False
                    break
            
            if not is_possible:
                ans |= (1 << bit)
                
        return ans