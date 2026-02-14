class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for ele in nums:
            if stack and stack[-1] == ele:
                curr = ele * 2
                stack.pop()
                while stack and stack[-1] == curr:
                    stack.pop()
                    curr *= 2
                stack.append(curr)
            else:
                stack.append(ele)
        return stack