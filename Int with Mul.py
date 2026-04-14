class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        dicc = {}
        limit = int(n**(1/3)) + 2
        
        for i in range(1, limit):
            i3 = i**3
            if i3 > n:
                break
            for j in range(i, limit):
                summ = i3 + j**3
                if summ > n:
                    break
                dicc[summ] = dicc.get(summ, 0) + 1
        
        final = [key for key, val in dicc.items() if val >= 2]
        final.sort()
        return final