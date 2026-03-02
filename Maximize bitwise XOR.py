class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        counts = {"0": 0, "1": 0}
        for char in t:
            counts[char] += 1
            
        final_xor = []
        
        for char in s:
            if char == "0":
                if counts["1"] > 0:
                    final_xor.append("1")
                    counts["1"] -= 1
                else:
                    final_xor.append("0")
                    counts["0"] -= 1
            else: 
                if counts["0"] > 0:
                    final_xor.append("1")
                    counts["0"] -= 1
                else:
                    final_xor.append("0")
                    counts["1"] -= 1
                    
        return "".join(final_xor)