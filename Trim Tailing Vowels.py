class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        letters=[]
        for ele in s:
            letters.append(ele)
        i=len(letters)-1
        while i>=0 and (letters[i] in "aeiou"):
            i-=1
        return "".join(letters[:i+1])
        