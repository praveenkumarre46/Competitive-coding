class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        dic={}
        for ele in bulbs:
            if ele in dic:
                dic[ele]+=1
            else:
                dic[ele]=1
        final=[]
        for key,val in dic.items():
            if val%2!=0:
                final.append(key)
        return sorted(final)
            